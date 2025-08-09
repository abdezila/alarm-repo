import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        # generate central_widget to display layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #create some labels
        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)
        #some stylesheets
        label1.setStyleSheet("background-color:blue;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:white;")
        label4.setStyleSheet("background-color:red;")
        label5.setStyleSheet("background-color:green;")
        #call grid layout
        grid = QGridLayout()
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)
        grid.addWidget(label4,1,0)
        grid.addWidget(label5,1,1)
        #link widget with layout
        central_widget.setLayout(grid)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
