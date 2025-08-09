import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
            #create button
        self.button = QPushButton("Clicke me!",self)
            #call method
        self.initUI()

    def initUI(self):
            #behavior of button
        self.button.setGeometry(150,150,200,100)
            #connect button with event(clicked)
        self.button.clicked.connect(self.on_click)
            #label
        self.label = QLabel("Hello",self)
        self.label.setGeometry(210,250,200,100)
        self.label.setStyleSheet("font-size:30px;")
            #events:
    def on_click(self):
        print("done!!")
        self.button.setText("Clicked")
        self.label.setText("bye")
        self.button.setDisabled(True)
#----------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ =="__main__":
    main()