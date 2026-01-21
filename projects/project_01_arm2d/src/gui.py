import matplotlib as plt
import PyQt5.QtWidgets as QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
from kinematics import positions_function

class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D Arm Model")
        self.setGeometry(100, 100, 800, 600)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.set_aspect('equal')
        R = 2 # l1+l2
        self.axes.set_xlim(-R, R)
        self.axes.set_ylim(-R, R)
        self.figureCanvas = FigureCanvas(self.figure)
        self.figureCanvas.setParent(self)
        self.setCentralWidget(self.figureCanvas)
        self.positions = positions_function(100*math.pi/180, -80*math.pi/180, 1, 1)
        self.axes.plot([self.positions[0][0],self.positions[1][0]],[self.positions[0][1],self.positions[1][1]])
        self.axes.plot([self.positions[1][0],self.positions[2][0]],[self.positions[1][1],self.positions[2][1]])
        self.figureCanvas.draw()


        

if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec_()