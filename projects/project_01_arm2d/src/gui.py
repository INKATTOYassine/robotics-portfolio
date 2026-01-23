import matplotlib as plt
import PyQt5.QtWidgets as QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
from kinematics import positions_function
from PyQt5.QtCore import Qt

APP_STYLE = """
    QMainWindow {
        background-color: #f5f5f7; 
    }
    QWidget {
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        font-size: 14px;
        color: #333333;
    }
    
    /* Headings and Labels */
    QLabel {
        color: #1d1d1f;
        font-weight: 600; /* Semi-bold for readability */
        margin-bottom: 2px;
    }

    /* Input Fields */
    QDoubleSpinBox {
        background-color: #ffffff;
        border: 1px solid #d2d2d7;
        border-radius: 6px; /* Soft rounding */
        padding: 6px;
        color: #1d1d1f;
        font-weight: 400;
    }
    QDoubleSpinBox:focus {
        border: 1px solid #0071e3; /* Pro Blue focus ring */
        background-color: #ffffff;
    }
    QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
        background-color: transparent;
        border: none;
        width: 20px;
    }

    /* Sliders */
    QSlider::groove:horizontal {
        border: 1px solid #d2d2d7;
        height: 4px;
        background: #e5e5ea;
        margin: 2px 0;
        border-radius: 2px;
    }
    QSlider::handle:horizontal {
        background: #ffffff;
        border: 1px solid #d2d2d7;
        width: 20px;
        height: 20px;
        margin: -9px 0; 
        border-radius: 10px; 
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    QSlider::handle:horizontal:hover {
        border-color: #0071e3; 
    }
"""

class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D Arm Model")
        self.setGeometry(100, 100, 800, 600)
        self.figure = Figure()
        self.figure.set_facecolor('#f5f5f7')
        self.figure.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_facecolor('#f5f5f7')
        self.axes.grid(True, color='#d2d2d7', linestyle='--')
        self.axes.set_aspect('equal')
        for spine in self.axes.spines.values():
            spine.set_visible(False)

        self.figureCanvas = FigureCanvas(self.figure)
        self.figureCanvas.setParent(self)
        main_container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        main_container.setLayout(layout)

        self.label_l1 = QtWidgets.QLabel("Length 1:")
        self.input_l1 = QtWidgets.QDoubleSpinBox()
        self.input_l1.setRange(0.1, 2000.0)
        self.input_l1.setValue(1.0)
        self.input_l1.setSingleStep(1) 

        self.row1 = QtWidgets.QHBoxLayout()
        self.row1.addWidget(self.label_l1)
        self.row1.addWidget(self.input_l1)
       
        self.label_l2 = QtWidgets.QLabel("Length 2:")
        self.input_l2 = QtWidgets.QDoubleSpinBox()
        self.input_l2.setRange(0.1, 2000.0)
        self.input_l2.setValue(1.0) 
        self.input_l2.setSingleStep(1)
        self.input_l1.valueChanged.connect(self.update_arm)
        self.input_l2.valueChanged.connect(self.update_arm)

        self.row2 = QtWidgets.QHBoxLayout()
        self.row2.addWidget(self.label_l2)
        self.row2.addWidget(self.input_l2)


        R = self.input_l1.value() + self.input_l2.value() # l1+l2
        self.axes.set_xlim(-R, R)
        self.axes.set_ylim(-R, R)


        self.slider_theta1 = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_theta1.setRange(-180,180)
        self.slider_theta2 = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_theta2.setRange(-180,180)


        self.control_group = QtWidgets.QGroupBox("Arm Parameters")
        self.control_group.setFixedWidth(300)


        self.controls_layout = QtWidgets.QVBoxLayout()
        self.control_group.setLayout(self.controls_layout)

# 3. Add ALL the controls here
        self.controls_layout.addLayout(self.row1)
        self.controls_layout.addLayout(self.row2)
        self.controls_layout.addWidget(self.slider_theta1)
        self.controls_layout.addWidget(self.slider_theta2)

        self.controls_layout.addStretch()
        layout.addWidget(self.control_group)
        layout.addWidget(self.figureCanvas, 1)


        self.slider_theta1.valueChanged.connect(self.update_arm)
        self.slider_theta2.valueChanged.connect(self.update_arm)
        self.setCentralWidget(main_container)
        self.positions = positions_function(100*math.pi/180, -80*math.pi/180, self.input_l1.value(), self.input_l2.value())
        self.axes.plot([self.positions[0][0],self.positions[1][0]],[self.positions[0][1],self.positions[1][1]])
        self.axes.plot([self.positions[1][0],self.positions[2][0]],[self.positions[1][1],self.positions[2][1]])
        self.figureCanvas.draw()

    def update_arm(self):
        self.axes.clear()
        R = self.input_l1.value() + self.input_l2.value() # l1+l2
        self.axes.set_xlim(-R, R)
        self.axes.set_ylim(-R, R)
        self.positions = positions_function(math.radians(self.slider_theta1.value()),math.radians(self.slider_theta2.value()),self.input_l1.value(),self.input_l2.value())
        self.axes.plot([self.positions[0][0],self.positions[1][0]],[self.positions[0][1],self.positions[1][1]])
        self.axes.plot([self.positions[1][0],self.positions[2][0]],[self.positions[1][1],self.positions[2][1]])
        self.axes.grid(True, color='#d2d2d7', linestyle='--')
        self.figureCanvas.draw()


        

if __name__ == "__main__":
        app = QtWidgets.QApplication([])
        app.setStyleSheet(APP_STYLE)
        window = MainWindow()
        window.show()
        app.exec_()