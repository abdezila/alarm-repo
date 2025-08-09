import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt,QTime,QTimer
class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer= QTimer(self)
        self.initUI()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
      

    def initUI(self):
        self.setWindowTitle("Digital_clock")
        self.setGeometry(600,400,300,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;"
                                      "font-family:Arial;"
                                      "color:#FFF9E5;"
                                      )
        self.setStyleSheet("background-color:#004030")
        self.update_time()
    

    def update_time(self):
        cerrent_time = QTime().currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(cerrent_time)







def main():
    app = QApplication(sys.argv)
    window = digital_clock()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()

















