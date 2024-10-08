# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(441, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/calculator-minimalistic-icon-2048x2046-73qvgwb6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(22, 60, 401, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_output = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.label_output.sizePolicy().hasHeightForWidth())
        self.label_output.setSizePolicy(sizePolicy)
        self.label_output.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.gridLayout.addWidget(self.label_output, 0, 0, 1, 4)
        self.pushButton_equalto = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_equalto.sizePolicy().hasHeightForWidth())
        self.pushButton_equalto.setSizePolicy(sizePolicy)
        self.pushButton_equalto.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_equalto.setObjectName("pushButton_equalto")
        self.gridLayout.addWidget(self.pushButton_equalto, 5, 3, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        self.pushButton_mul.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 3, 3, 1, 1)
        self.push_del = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.push_del.sizePolicy().hasHeightForWidth())
        self.push_del.setSizePolicy(sizePolicy)
        self.push_del.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.push_del.setObjectName("push_del")
        self.gridLayout.addWidget(self.push_del, 1, 2, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_plus.setSizePolicy(sizePolicy)
        self.pushButton_plus.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 1, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_point = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_point.sizePolicy().hasHeightForWidth())
        self.pushButton_point.setSizePolicy(sizePolicy)
        self.pushButton_point.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_point.setObjectName("pushButton_point")
        self.gridLayout.addWidget(self.pushButton_point, 5, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_divide.sizePolicy().hasHeightForWidth())
        self.pushButton_divide.setSizePolicy(sizePolicy)
        self.pushButton_divide.setStyleSheet("background-color: rgb(170, 170, 0);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 4, 3, 1, 1)
        self.pushButton_zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_zero.sizePolicy().hasHeightForWidth())
        self.pushButton_zero.setSizePolicy(sizePolicy)
        self.pushButton_zero.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.gridLayout.addWidget(self.pushButton_zero, 5, 0, 1, 2)
        self.push_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.push_clear.sizePolicy().hasHeightForWidth())
        self.push_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_clear.setFont(font)
        self.push_clear.setMouseTracking(True)
        self.push_clear.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.push_clear.setObjectName("push_clear")
        self.gridLayout.addWidget(self.push_clear, 1, 0, 1, 2)
        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        self.pushButton_minus.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 0);")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 2, 3, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 18))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        
 

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "CalculatorGui"))
        self.pushButton_equalto.setText(_translate("mainWindow", "="))
        self.pushButton_mul.setText(_translate("mainWindow", "X"))
        self.push_del.setText(_translate("mainWindow", "Delete"))
        self.pushButton_plus.setText(_translate("mainWindow", "+"))
        self.pushButton_5.setText(_translate("mainWindow", "5"))
        self.pushButton_1.setText(_translate("mainWindow", "1"))
        self.pushButton_4.setText(_translate("mainWindow", "4"))
        self.pushButton_7.setText(_translate("mainWindow", "7"))
        self.pushButton_2.setText(_translate("mainWindow", "2"))
        self.pushButton_8.setText(_translate("mainWindow", "8"))
        self.pushButton_3.setText(_translate("mainWindow", "3"))
        self.pushButton_point.setText(_translate("mainWindow", "."))
        self.pushButton_9.setText(_translate("mainWindow", "9"))
        self.pushButton_6.setText(_translate("mainWindow", "6"))
        self.pushButton_divide.setText(_translate("mainWindow", "/"))
        self.pushButton_zero.setText(_translate("mainWindow", "0"))
        self.push_clear.setText(_translate("mainWindow", "Clear"))
        self.pushButton_minus.setText(_translate("mainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
