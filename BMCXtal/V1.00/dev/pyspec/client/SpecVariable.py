#  @(#)SpecVariable.py	3.5  05/11/20 CSS
#  "pyspec" Release 3
#
#$Id: SpecVariable.py,v 1.4 2005/03/17 12:43:46 guijarro Exp $

"""SpecVariable module

This module defines the class for Spec variable objects
"""

__author__ = 'Matias Guijarro'
__version__ = '1.0'

import SpecConnectionsManager as SpecConnectionsManager
import SpecEventsDispatcher as SpecEventsDispatcher
import SpecWaitObject as SpecWaitObject

(UPDATEVALUE, FIREEVENT) = (SpecEventsDispatcher.UPDATEVALUE, SpecEventsDispatcher.FIREEVENT)

class SpecVariable:
    """SpecVariable class

    Thin wrapper around SpecChannel objects, to make
    variables watching, setting and getting values easier.
    """
    def __init__(self, varName = None, specVersion = None, timeout = None, prefix=True):
        """Constructor

        Keyword arguments:
        varName -- the variable name in Spec
        specVersion -- 'host:port' string representing a Spec server to connect to (defaults to None)
        timeout -- optional timeout (defaults to None)
        """
        self.connection = None
        self.isConnected = self.isSpecConnected #alias

        if varName is not None and specVersion is not None:
            self.connectToSpec(varName, specVersion, timeout, prefix)
        else:
            self.channelName = None
            self.specVersion = None


    def connectToSpec(self, varName, specVersion, timeout = None, prefix=True):
        """Connect to a remote Spec

        Connect to Spec

        Arguments:
        varName -- the variable name in Spec
        specVersion -- 'host:port' string representing a Spec server to connect to
        timeout -- optional timeout (defaults to None)
        """
        if prefix:
          self.channelName = 'var/' + str(varName)
        else:
          self.channelName = str(varName)
        self.specVersion = specVersion

        if isinstance(specVersion, str):
            self.connection = SpecConnectionsManager.SpecConnectionsManager().getConnection(specVersion)
        else:
            self.connection = specVersion

        w = SpecWaitObject.SpecWaitObject(self.connection)
        w.waitConnection(timeout)


    def isSpecConnected(self):
        """Return whether the remote Spec version is connected or not."""
        return self.connection is not None and self.connection.isSpecConnected()


    def getValue(self):
        """Return the watched variable current value."""
        chan = self.connection.getChannel(self.channelName)

        return chan.read()


    def setValue(self, value):
        """Set the watched variable value

        Arguments:
        value -- the new variable value
        """
        if self.isConnected():
            chan = self.connection.getChannel(self.channelName)

            return chan.write(value)


    def waitUpdate(self, waitValue = None, timeout = None):
        """Wait for the watched variable value to change

        Keyword arguments:
        waitValue -- wait for a specific variable value
        timeout -- optional timeout
        """
        if self.isConnected():
            w = SpecWaitObject.SpecWaitObject(self.connection)

            w.waitChannelUpdate(self.channelName, waitValue = waitValue, timeout = timeout)

            return w.value


class SpecVariableA:
    """SpecVariableA class - asynchronous version of SpecVariable

    Thin wrapper around SpecChannel objects, to make
    variables watching, setting and getting values easier.
    """
    def __init__(self, varName = None, specVersion = None, dispatchMode = UPDATEVALUE, prefix=True, callbacks={}):
        """Constructor

        Keyword arguments:
        varName -- name of the variable to monitor (defaults to None)
        specVersion -- 'host:port' string representing a Spec server to connect to (defaults to None)
        """
        self.connection = None
        self.dispatchMode = UPDATEVALUE
        self.channelName = ''
        self.__callbacks = {
          'connected': None,
          'disconnected': None,
          'update': None,
        }
        for cb_name in iter(self.__callbacks.keys()):
          if callable(callbacks.get(cb_name)):
            self.__callbacks[cb_name] = SpecEventsDispatcher.callableObjectRef(callbacks[cb_name])


        if varName is not None and specVersion is not None:
            self.connectToSpec(varName, specVersion, dispatchMode = dispatchMode, prefix=prefix)
        else:
            self.varName = None
            self.specVersion = None


    def connectToSpec(self, varName, specVersion, dispatchMode = UPDATEVALUE, prefix=True):
        """Connect to a remote Spec

        Connect to Spec and register channel for monitoring variable

        Arguments:
        varName -- name of the variable
        specVersion -- 'host:port' string representing a Spec server to connect to
        """
        self.varName = varName
        self.specVersion = specVersion
        if prefix:
          self.channelName = 'var/%s' % varName
        else:
          self.channelName = varName

        if isinstance(specVersion,str):
            self.connection = SpecConnectionsManager.SpecConnectionsManager().getConnection(specVersion)
        else:
            self.connection = specVersion
        self.connection.connect('connected', self._connected)
        self.connection.connect('disconnected', self._disconnected)
        self.dispatchMode = dispatchMode

        if self.connection.isSpecConnected():
            self._connected()

    def refresh(self):
        self.connection.update()

    def isSpecConnected(self):
        return self.connection is not None and self.connection.isSpecConnected()


    def _connected(self):
        #
        # register channel
        #
        self.connection.registerChannel(self.channelName, self._update, dispatchMode = self.dispatchMode)

        self.connection.send_msg_hello()

        try:
          if self.__callbacks.get("connected"):
            cb = self.__callbacks["connected"]()
            if cb is not None:
              cb()
        finally:
            self.connected()


    def connected(self):
        """Callback triggered by a 'connected' event from Spec

        To be extended by derivated classes.
        """
        pass


    def _disconnected(self):
        try:
          if self.__callbacks.get("disconnected"):
            cb = self.__callbacks["disconnected"]()
            if cb is not None:
              cb()
        finally:
          self.disconnected()


    def disconnected(self):
        """Callback triggered by a 'disconnected' event from Spec

        To be extended by derivated classes.
        """
        pass


    def _update(self, value):
        try:
          if self.__callbacks.get("update"):
            cb = self.__callbacks["update"]()
            if cb is not None:
              cb(value)
        finally:
          self.update(value)
        

    def update(self, value):
        """Callback triggered by a variable update

        Extend it to do something useful.
        """
        pass


    def getValue(self):
        """Return the watched variable current value."""
        if self.connection is not None:
            chan = self.connection.getChannel(self.channelName)

            return chan.read()


    def setValue(self, value):
        """Set the watched variable value

        Arguments:
        value -- the new variable value
        """
        if self.connection is not None:
            chan = self.connection.getChannel(self.channelName)

            return chan.write(value)
