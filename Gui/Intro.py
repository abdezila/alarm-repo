#PyQt5 introduction
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
    #import icon
# from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

            #set icon on app:
        # self.setWindowIcon(QIcon("/home/kali/Downloads/cat.jpg"))

            #some geometry on app
        self.setGeometry(700,300,500,500)
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        #-------------------------------------------------------------
        #Create image
            #create object of image
            # pixmap = QPixmap("/home/kali/Desktop/Pyhon/Gui/tiger.jpeg")
                 #link image with label:
            # label.setPixmap(pixmap)
            #     #to get all content:
            # label.setScaledContents(True)
            #     #position of image:
            # label.setGeometry((self.width() - label.width()) //2,
            #                   (self.height() - label.height()) //2,
            #                    label.width(),
            #                    label.height())
        #     #add title on app
        # self.setWindowTitle("Abdou")
            #theme:
        # label = QLabel("Abdou",self)
        # label.setFont(QFont("Arial",40))
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet("color: #CFFFE2;""background-color:#000000;""font-weight:bold;""font-style: italic")
            #Positions:
        #label.setAlignment(Qt.AlignTop)     #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom)  #VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter) #VERTICALLY CENTER
        #-------------------------------------------------------
        #label.setAlignment(Qt.AlignRight)   #HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignLeft)    #HORIZONTALLY LEFT
        #label.setAlignment(Qt.AlignHCenter) #HORIZONTALLY CENTER
                    #Together:
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()