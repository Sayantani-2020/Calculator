from PyQt5 import QtWidgets
from calculator_ui import Ui_mainWindow

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.pushButton_1.clicked.connect(self.method_1)
        self.ui.pushButton_2.clicked.connect(self.method_2)
        self.ui.pushButton_3.clicked.connect(self.method_3)
        self.ui.pushButton_4.clicked.connect(self.method_4)
        self.ui.pushButton_5.clicked.connect(self.method_5)
        self.ui.pushButton_6.clicked.connect(self.method_6)
        self.ui.pushButton_7.clicked.connect(self.method_7)
        self.ui.pushButton_8.clicked.connect(self.method_8)
        self.ui.pushButton_9.clicked.connect(self.method_9)
        self.ui.push_del.clicked.connect(self.method_del)
        self.ui.push_clear.clicked.connect(self.method_clear)
        self.ui.pushButton_minus.clicked.connect(self.method_minus)
        self.ui.pushButton_divide.clicked.connect(self.method_divide)
        self.ui.pushButton_mul.clicked.connect(self.method_mul)
        self.ui.pushButton_equalto.clicked.connect(self.method_equalto)
        self.ui.pushButton_point.clicked.connect(self.method_point)
        self.ui.pushButton_plus.clicked.connect(self.method_plus)


    def method_1(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "1") # Append "1" to the current text and update the label

    def method_2(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "2")

    def method_3(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "3")

    def method_4(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "4")
   
    def method_5(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "5")

    def method_6(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "6")

    def method_7(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "7")

    def method_8(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "8")

    def method_9(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "9")

    def method_plus(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "+")
    def method_minus(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "-")
    def method_mul(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "*")
    def method_divide(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + "/")
    def method_point(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text + ".")
    def method_clear(self):
        self.ui.label_output.setText("")

    def method_del(self):
        text = self.ui.label_output.text() # Get the current text from the label
        self.ui.label_output.setText(text[:len(text)-1])
    def method_equalto(self):
        text = self.ui.label_output.text()
        try:
            ans = eval(text)
            self.ui.label_output.setText(str(ans))
        except:
             self.ui.label_output.setText("Error occurred")
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj =MainWin()
    sys.exit(app.exec_())
    