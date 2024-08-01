# python3
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.uic import loadUi
from main_window_ui import Ui_MainWindow
import pyqtgraph as pg
from random import randint
import sys

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_Find_and_Replace.triggered.connect(self.findAndReplace)
        self.action_About.triggered.connect(self.about)
        self.start.clicked.connect(self.displayGraph)

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    def displayGraph(self):

        self.x = list(range(100))                      # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.plot_widget_1.plot(self.x, self.y, pen=pen)

        # set timer
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("gui/find_replace.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
