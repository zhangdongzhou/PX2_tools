import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QScrollArea, QGroupBox, QLineEdit, QFrame, 
    QFileDialog
)
# from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline
import os

class InteractiveCanvas(FigureCanvas):
    def __init__(self, on_line_moved):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.on_line_moved = on_line_moved

        self.ax.plot(range(10))  # Dummy plot
        self.vline1 = None
        self.vline2 = None
        self.active_line = None

        self.setMouseTracking(True)
        self.mpl_connect("button_press_event", self.on_click)
        self.mpl_connect("motion_notify_event", self.on_motion)
        self.mpl_connect("button_release_event", self.on_release)

    def show_lines(self, x1, x2):
        # Create or update vertical line 1
        if self.vline1 is None:
            self.vline1 = self.ax.axvline(x=x1, color='r')
        else:
            self.vline1.set_xdata(x1)
            self.vline1.set_visible(True)

        # Create or update vertical line 2
        if self.vline2 is None:
            self.vline2 = self.ax.axvline(x=x2, color='r')
        else:
            self.vline2.set_xdata(x2)
            self.vline2.set_visible(True)

        self.draw()


    def hide_lines(self):
        self.vline1.set_visible(False)
        self.vline2.set_visible(False)
        self.draw()

    def update_line_from_input(self, line, x):
        if line == "vline1":
            self.vline1.set_xdata(x)
        elif line == "vline2":
            self.vline2.set_xdata(x)
        self.draw()

    def on_click(self, event):
        if not event.inaxes:
            return
        x1 = float(self.vline1.get_xdata())
        x2 = float(self.vline2.get_xdata())

        if abs(event.xdata - x1) < 0.3*abs(x1-x2):
            self.active_line = "vline1"
        elif abs(event.xdata - x2) < 0.3*abs(x1-x2):
            self.active_line = "vline2"

    def on_motion(self, event):
        if self.active_line and event.inaxes:
            new_x = event.xdata
            if self.active_line == "vline1":
                self.vline1.set_xdata(new_x)
            elif self.active_line == "vline2":
                self.vline2.set_xdata(new_x)
            self.draw()
            self.on_line_moved(self.active_line, new_x)

    def on_release(self, event):
        self.active_line = None


class GroupBoxWidget(QGroupBox):
    def __init__(self, index, on_select, on_lineedit_change, on_remove, x1_init=2.0, x2_init=7.0):
        super().__init__(f"Peak {index}")
        self.index = index
        self.on_select = on_select
        self.on_lineedit_change = on_lineedit_change
        self.on_remove = on_remove

        self.line_edit1 = QLineEdit(f"{x1_init:.2f}")
        self.line_edit2 = QLineEdit(f"{x2_init:.2f}")
        self.select_button = QPushButton("Select")
        self.remove_button = QPushButton("Remove")

        layout = QHBoxLayout()
        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)
        layout.addWidget(self.select_button)
        layout.addWidget(self.remove_button)
        self.setLayout(layout)

        self.select_button.clicked.connect(self.select)
        self.remove_button.clicked.connect(self.remove)
        self.line_edit1.editingFinished.connect(self.edit_line1)
        self.line_edit2.editingFinished.connect(self.edit_line2)

    def highlight(self, active=True):
            if active:
                self.setStyleSheet("""
                    QGroupBox {
                        border: 2px solid blue;
                        margin-top: 6px;
                    }
                    QGroupBox:title {
                        subcontrol-origin: margin;
                        left: 10px;
                        padding: 0 3px 0 3px;
                    }
                """)
            else:
                self.setStyleSheet("")

    def select(self):
        self.on_select(self)

    def remove(self):
        self.on_remove(self)

    def edit_line1(self):
        try:
            x = float(self.line_edit1.text())
            self.on_lineedit_change(self, "vline1", x)
        except ValueError:
            pass

    def edit_line2(self):
        try:
            x = float(self.line_edit2.text())
            self.on_lineedit_change(self, "vline2", x)
        except ValueError:
            pass

    def set_values(self, x1, x2):
        self.line_edit1.setText(f"{x1:.2f}")
        self.line_edit2.setText(f"{x2:.2f}")



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("13BMC Online Raman Filter")
        self.selected_box = None

        main_layout = QHBoxLayout(self)

        # LEFT PANEL
        self.canvas1 = InteractiveCanvas(self.on_line_moved)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        
        self.canvas2 = FigureCanvas(plt.Figure())
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        
        self.canvas2.ax2 = self.canvas2.figure.add_subplot(111)
        # self.ax2.plot([0, 1, 2], [2, 1, 3])
        
        self.load_button = QPushButton("Load File")
        
        self.path_line_edit = QLineEdit()
        # self.path_line_edit.setReadOnly(True)
        
        top_left_layout = QHBoxLayout()
        top_left_layout.addWidget(self.load_button)
        top_left_layout.addWidget(self.path_line_edit)

        self.load_button.clicked.connect(self.load_txt_file)
        
        left_layout = QVBoxLayout()
        left_layout.addLayout(top_left_layout)
        left_layout.addWidget(self.toolbar1)
        left_layout.addWidget(self.canvas1)
        left_layout.addWidget(self.toolbar2)
        left_layout.addWidget(self.canvas2)

        
        left_frame = QFrame()
        left_frame.setLayout(left_layout)
        main_layout.addWidget(left_frame, stretch=2)



        # Right panel
        # self.add_button = QPushButton("AddB")
        # self.add_button.clicked.connect(self.add_group_box)
        self.add_button = QPushButton("Add")
        self.filter_button = QPushButton("Filter")
        
        self.export_button = QPushButton("Export")

        
        self.add_button.clicked.connect(self.add_group_box)
        self.filter_button.clicked.connect(self.filter_action)
        self.export_button.clicked.connect(self.export_action) # define this later
        self.path_line_edit.returnPressed.connect(self.load_from_path_edit)
        


        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_content)

        # Put both buttons in a horizontal layout
        top_right_button_layout = QHBoxLayout()
        top_right_button_layout.addWidget(self.add_button)
        top_right_button_layout.addWidget(self.filter_button)
        self.smooth_input = QLineEdit()
        self.smooth_input.setPlaceholderText("Smoothing")
        self.smooth_input.setFixedWidth(100)
        top_right_button_layout.addWidget(self.smooth_input)
        top_right_button_layout.addWidget(self.export_button)
        
        right_layout = QVBoxLayout()
        right_layout.addLayout(top_right_button_layout)
        right_layout.addWidget(self.scroll_area)
        right_frame = QFrame()
        right_frame.setLayout(right_layout)
        main_layout.addWidget(right_frame, stretch=1)

        self.group_boxes = []

    def add_group_box(self):
        idx = len(self.group_boxes) + 1
        xlim = self.canvas1.ax.get_xlim()
        if xlim[0] == xlim[1]:  # fallback for empty plot
            x1, x2 = 2.0, 7.0
        else:
            x1 = xlim[0] + 0.2 * (xlim[1] - xlim[0])
            x2 = xlim[0] + 0.7 * (xlim[1] - xlim[0])
    
        box = GroupBoxWidget(
            idx,
            self.select_box,
            self.on_lineedit_change,
            self.remove_group_box,
            x1_init=x1,
            x2_init=x2
        )
        self.scroll_layout.addWidget(box)
        self.group_boxes.append(box)
        # self.selected_box = box
        # self.select_box(box)  
        box.select()



    def select_box(self, box):
        if self.selected_box:
            self.selected_box.highlight(False)
        self.selected_box = box
        box.highlight(True)
    
        try:
            x1 = float(box.line_edit1.text())
            x2 = float(box.line_edit2.text())
            self.canvas1.show_lines(x1, x2)
        except ValueError:
            self.canvas1.hide_lines()


    def on_line_moved(self, line, new_x):
        if self.selected_box:
            if line == "vline1":
                self.selected_box.line_edit1.setText(f"{new_x:.2f}")
            elif line == "vline2":
                self.selected_box.line_edit2.setText(f"{new_x:.2f}")

    def on_lineedit_change(self, box, line, x):
        if self.selected_box == box:
            self.canvas1.update_line_from_input(line, x)
    
    def load_txt_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt)")
        if file_path:
            try:
                data = np.loadtxt(file_path)
                if data.shape[1] < 2:
                    print("The file must have at least two columns.")
                    return
                x = data[:, 0]
                y = data[:, 1]
                self.canvas1.ax.cla()
                self.canvas1.ax.plot(x, y, color='blue')
                self.canvas1.ax.set_xlim(min(x), max(x))
                self.set_default_labels()
                self.canvas1.draw()
                self.path_line_edit.setText(file_path)  
                
                self.smooth_input.setText(str(5 * len(x)))
            except Exception as e:
                print(f"Error loading file: {e}")
    
    def remove_group_box(self, box):
        self.scroll_layout.removeWidget(box)
        box.setParent(None)
        self.group_boxes.remove(box)
        if self.selected_box == box:
            self.selected_box = None
            self.canvas1.hide_lines()
    
    def set_default_labels(self):
        self.canvas1.ax.set_xlabel("Wave number (cm$^{-1}$)")
        self.canvas1.ax.set_ylabel("Intensity (a.u.)")
        self.canvas2.ax2.set_xlabel("Wave number (cm$^{-1}$)")
        self.canvas2.ax2.set_ylabel("Intensity (a.u.)")

            
    def filter_action(self):

    # Step 1: Collect filter ranges from group boxes
        filter_data = []
        for box in self.group_boxes:
            try:
                x1 = float(box.line_edit1.text())
                x2 = float(box.line_edit2.text())
                if x1 < x2:
                    filter_data.append([x1, x2])
                else:
                    filter_data.append([x2, x1])  # Ensure x1 < x2
            except ValueError:
                pass
    
        if not filter_data:
            print("No valid group boxes found.")
            return
    
        filter_array = np.array(filter_data)
        print("Filter ranges:")
        print(filter_array)
    
        # Step 2: Get original plot data
        try:
            line = self.canvas1.ax.lines[0]
            xdata = np.array(line.get_xdata())
            ydata = np.array(line.get_ydata())
        except IndexError:
            print("No plot data found.")
            return
    
        # Step 3: Build masks
        keep_mask = np.ones_like(xdata, dtype=bool)  # Default: keep everything
        for x1, x2 in filter_array:
            keep_mask &= ~((xdata > x1) & (xdata < x2))  # Remove points inside ranges
    
        # Invert to get removed points
        remove_mask = ~keep_mask
    
        x_keep = xdata[keep_mask]
        y_keep = ydata[keep_mask]
        x_remove = xdata[remove_mask]
        # y_remove = ydata[remove_mask]
        
        try:
            s_value = float(self.smooth_input.text())
        except ValueError:
            s_value = len(x_keep) * 5  # default fallback
        
        smoothed = UnivariateSpline(x_keep, y_keep, s=s_value)
        # smoothed = UnivariateSpline(x_keep,y_keep,s=len(x_keep)*5)
        BKG= smoothed(xdata)
    
        print(f"Keeping {len(x_keep)} pts, removing {len(x_remove)} pts.")
    
        # Step 4: Plot both sets of data
        # Save the current vline positions
        x1 = self.canvas1.vline1.get_xdata()
        x2 = self.canvas1.vline2.get_xdata()
        self.canvas1.ax.clear()
        self.canvas2.ax2.clear()
        self.canvas1.ax.plot(xdata, ydata, color='blue', label='Original')  # Base plot
        # Replace the original line data
        # line = self.canvas1.ax.lines[0]  # Original data line
        # line.set_ydata(ydata)           # Optionally update it
        # line.set_xdata(xdata)
        if len(x_keep) > 0:
            self.canvas1.ax.plot(xdata, BKG, '-', color='cyan', label='Background')
        
        self.canvas2.ax2.plot(xdata, ydata-BKG, color='blue', label='Filtered')
    
        self.canvas1.ax.legend()
        self.canvas1.ax.relim()
        self.canvas1.ax.set_xlim(min(xdata), max(xdata))
        self.canvas1.ax.autoscale_view()
        self.canvas1.vline1 = self.canvas1.ax.axvline(x=x1, color='r')
        self.canvas1.vline2 = self.canvas1.ax.axvline(x=x2, color='r')

        self.set_default_labels()
        self.canvas1.draw()
    
        # self.canvas1.hide_lines()
        # self.selected_box = None
        
        if self.selected_box:
            self.selected_box.highlight(False)
            self.selected_box = None
        
        self.canvas1.hide_lines()
        self.canvas2.ax2.legend()
        self.canvas2.ax2.relim()
        self.canvas2.ax2.set_xlim(min(xdata), max(xdata))
        self.canvas2.ax2.autoscale_view()
        self.canvas2.draw()
    

    def load_from_path_edit(self):
    # import os
    # import numpy as np

        file_path = self.path_line_edit.text()
        if os.path.isfile(file_path):
            try:
                data = np.loadtxt(file_path)
                if data.shape[1] < 2:
                    print("File must have at least two columns.")
                    return
                x, y = data[:, 0], data[:, 1]
                self.canvas1.ax.cla()
                self.canvas1.ax.plot(x, y, color='blue')
                self.canvas1.ax.set_xlim(min(x), max(x))
                self.canvas1.ax.set_xlabel("Wave number (cm$^{-1}$)")
                self.canvas1.ax.set_ylabel("Intensity (a.u.)")
                self.canvas1.draw()
    
                self.smooth_input.setText(str(5 * len(x)))
            except Exception as e:
                print(f"Error loading file: {e}")
                self.path_line_edit.setText("")
        else:
            print("Invalid file path.")
            self.path_line_edit.setText("")
        
    def export_action(self):
        # Step 1: Get data from canvas2
        try:
            line = self.canvas2.ax2.lines[0]
            xdata = np.array(line.get_xdata())
            ydata = np.array(line.get_ydata())
        except IndexError:
            print("No filtered data to export.")
            return
    
        # Step 2: Prompt for save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Filtered Data", "", "Text Files (*.txt);;All Files (*)"
        )
        if not file_path:
            return  # User canceled
    
        # Step 3: Save data
        try:
            np.savetxt(file_path, np.column_stack((xdata, ydata)), fmt="%.6f", delimiter="\t",
                       header="Wave number (cm^-1)\tFiltered Intensity (a.u.)")
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"Error saving file: {e}")    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(1200, 700)
    win.show()
    sys.exit(app.exec_())
