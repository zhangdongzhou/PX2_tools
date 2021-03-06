#  @(#)SpecCommand.py	3.4  05/11/20 CSS
#  "pyspec" Release 3
#
"""SpecCommand module
.
This module defines the classes Spec command
objects

Classes:
BaseSpecCommand
SpecCommand
SpecCommandA
"""

__author__ = 'Matias Guijarro'
__version__ = '1.0'

import sys

from pyspec.css_logger import log
from pyspec.utils import is_python2

from SpecConnection import SpecClientNotConnectedError
from SpecReply import SpecReply
from SpecConnectionsManager import SpecConnectionsManager
import SpecEventsDispatcher as SpecEventsDispatcher
from SpecWaitObject import waitReply, waitConnection
from SpecClientError import SpecClientTimeoutError

class BaseSpecCommand:
    """Base class for SpecCommand objects"""
    def __init__(self, command = None, connection = None, callbacks = None):
        self.command = None
        self.connection = None
        self.specVersion = None
        self.isConnected = self.isSpecConnected #alias

        if isinstance(connection, str) or (is_python2() and isinstance(connection, unicode)):
            #
            # connection is given in the 'host:port' form
            #
            self.connectToSpec(str(connection))
        else:
            self.connection = connection

        if command is not None:
            self.setCommand(command)


    def connectToSpec(self, specVersion):
        pass


    def isSpecConnected(self):
        return self.connection is not None and self.connection.isSpecConnected()


    def isSpecReady(self):
        if self.isSpecConnected():
            try:
                status_channel = self.connection.getChannel("status/ready")
                status = status_channel.read()
            except:
                pass
            else:
                return status

        return False


    def setCommand(self, command):
        self.command = command


    def __repr__(self):
        return '<SpecCommand object, command=%s>' % self.command or ''


    def __call__(self, *args, **kwargs):
        if self.command is None:
            return

        if self.connection is None or not self.connection.isSpecConnected():
            return

        if self.connection.serverVersion < 3:
            func = False

            if 'function' in kwargs:
                func = kwargs['function']

            #convert args list to string args list
            #it is much more convenient using .call('psvo', 12) than .call('psvo', '12')
            #a possible problem will be seen in Spec
            args = map(repr, args)

            if func:
                # macro function
                command = self.command + '(' + ','.join(args) + ')'
            else:
                # macro
                command = self.command + ' ' + ' '.join(args)
        else:
            # Spec knows
            command = [self.command] + list(args)

        return self.executeCommand(command)


    def executeCommand(self, command):
        pass



class SpecCommand(BaseSpecCommand):
    """SpecCommand objects execute macros and wait for results to get back"""
    def __init__(self, command, connection=None, timeout = None):
        self.__timeout = timeout
        BaseSpecCommand.__init__(self, command, connection)


    def connectToSpec(self, specVersion):
        self.connection = SpecConnectionsManager().getConnection(specVersion)
        self.specVersion = specVersion

        waitConnection(self.connection, self.__timeout)


    def executeCommand(self, command):
        if self.connection.serverVersion < 3:
            connectionCommand = 'send_msg_cmd_with_return'
        else:
            if isinstance(command,str):
                connectionCommand = 'send_msg_cmd_with_return'
            else:
                connectionCommand = 'send_msg_func_with_return'

        return waitReply(self.connection, connectionCommand, (command, ), self.__timeout)



class SpecCommandA(BaseSpecCommand):
    """SpecCommandA is the asynchronous version of SpecCommand.
    It allows custom waiting by subclassing."""
    def __init__(self, *args, **kwargs):
        self.__callback = None
        self.__error_callback = None
        self.__callbacks = {
          'connected': None,
          'disconnected': None,
          'statusChanged': None,
        }
        callbacks = kwargs.get("callbacks", {})
        for cb_name in iter(self.__callbacks.keys()):
          if callable(callbacks.get(cb_name)):
            self.__callbacks[cb_name] = SpecEventsDispatcher.callableObjectRef(callbacks[cb_name])

        BaseSpecCommand.__init__(self, *args, **kwargs)


    def connectToSpec(self, specVersion, timeout=200):
        if self.connection is not None:
            SpecEventsDispatcher.disconnect(self.connection, 'connected', self._connected)
            SpecEventsDispatcher.disconnect(self.connection, 'disconnected', self._disconnected)

        self.connection = SpecConnectionsManager().getConnection(specVersion)
        self.specVersion = specVersion

        SpecEventsDispatcher.connect(self.connection, 'connected', self._connected)
        SpecEventsDispatcher.connect(self.connection, 'disconnected', self._disconnected)

        if self.connection.isSpecConnected():
            self._connected()
        else:
            try:
              waitConnection(self.connection, timeout)
            except SpecClientTimeoutError:
              pass
            SpecEventsDispatcher.dispatch()

    def connected(self):
        pass

    def _connected(self):
        self.connection.registerChannel("status/ready", self._statusChanged)
 
        self.connection.send_msg_hello()        

        try:
            cb_ref = self.__callbacks.get("connected")
            if cb_ref is not None:
                cb = cb_ref()
                if cb is not None:
                    cb()
        finally:
            self.connected()

    def _disconnected(self):
        try:
            cb_ref = self.__callbacks.get("disconnected")
            if cb_ref is not None:
                cb = cb_ref()
                if cb is not None:
                    cb()
        finally:
           self.disconnected()


    def disconnected(self):
        pass

 
    def _statusChanged(self, ready):
        try:
            cb_ref = self.__callbacks.get("statusChanged")
            if cb_ref is not None:
                cb = cb_ref()
                if cb is not None:
                   cb(ready)
        finally:
            self.statusChanged(ready)
    

    def statusChanged(self, ready):
        pass


    def executeCommand(self, command):
        self.beginWait()

        if self.connection.serverVersion < 3:
            id = self.connection.send_msg_cmd_with_return(command)
        else:
            if isinstance(command,str):
                id = self.connection.send_msg_cmd_with_return(command)
            else:
                id = self.connection.send_msg_func_with_return(command)


    def __call__(self, *args, **kwargs):
        log.log(2,"executing spec command")
        self.__callback = kwargs.get("callback", None)
        self.__error_callback = kwargs.get("error_callback", None)

        return BaseSpecCommand.__call__(self, *args, **kwargs)


    def replyArrived(self, reply):
        if reply.error:
            if callable(self.__error_callback):
                try:
                    self.__error_callback(reply.error)
                except:
                    log.exception("Error while calling error callback (command=%s,spec version=%s)", self.command, self.specVersion)
                self.__error_callback = None
        else:
            if callable(self.__callback):
                try:
                    self.__callback(reply.data)
                except:
                    log.exception("Error while calling reply callback (command=%s,spec version=%s)", self.command, self.specVersion)
                self.__callback = None


    def beginWait(self):
        pass


    def abort(self):
        if self.connection is None or not self.connection.isSpecConnected():
            return

        self.connection.abort()













