# python3
from PySide6.QtWidgets import QApplication, QMainWindow
#from PySide6 import QtCore
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [50,35,44,22,38,32,27,38,32,44]

        # set backgroun color
        self.graphWidget.setBackground('w')

        # graph title
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        # axis labels
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
        # legend
        self.graphWidget.addLegend()
        # background grid
        self.graphWidget.showGrid(x=True, y=True)

        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
