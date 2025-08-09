#PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QPushButton
    #import icon
# from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Submit",self)
        self.setGeometry(700,300,500,500)
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        self.line_edit = QLineEdit(self)
        self.initUI()
        
       
    def initUI(self):
        self.line_edit.setGeometry(10,10,250,40)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family:Arail;")
        
        self.button.setGeometry(260,10,90,40)
        self.button.setStyleSheet("font-size:20px;"
                                  "font-family:Arail;")
        self.button.clicked.connect(self.Submit)
        self.line_edit.setPlaceholderText("Enter your name")

    def Submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")
        
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()