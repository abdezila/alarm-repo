import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
            #create radios objects:
        self.radio1 = QRadioButton("visa",self)
        self.radio2 = QRadioButton("Master card",self)
        self.radio3 = QRadioButton("Gift card",self)
        self.radio4 = QRadioButton("in-store",self)
        self.radio5 = QRadioButton("online",self)
            #create button groups:
        self.button_Group1 = QButtonGroup()
        self.button_Group2 = QButtonGroup()

        self.initUI()

    def initUI(self):
            #set geametry of each radio:
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0,150,300,50)
        self.radio5.setGeometry(0,200,300,50)
            #grouped radios on specific group:
        self.button_Group1.addButton(self.radio1)
        self.button_Group1.addButton(self.radio2)
        self.button_Group1.addButton(self.radio3)
        self.button_Group2.addButton(self.radio4)
        self.button_Group2.addButton(self.radio5)
            #stylesheet of radios:
        self.setStyleSheet("QRadioButton{"
                "font-size : 40px;"
                "}")
            #link radios with event method(radio_button_change):
        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)
        #event method
    def radio_button_change(self):
            #sender responcible of how send the signals
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is checked")





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()