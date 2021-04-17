from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_MainWindowII(object):
    def setupUi(self, MainWindowII):
        MainWindowII.setObjectName("MainWindowII")
        MainWindowII.setFixedSize(800, 600)
        MainWindowII.setStyleSheet("QMainWindow {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 white, stop: 0.4 rgba(146,146,146,1),\n"
"stop:1 rgb(242,242,255))\n"
"}\n"
"\n"
"QTextEdit {\n"
"background: #c6c6c6;\n"
"}\n"
"\n"
"QPushButton {\n"
"background: #c6c6c6;\n"
"border: 1px solid #7f3a19;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ffff52;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #7bb87b;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindowII)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 30, 700, 500))
        self.textEdit.setFont(QtGui.QFont('Georgia', 16))
        self.textEdit.setText("")
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 550, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 550, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindowII.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowII)
        QtCore.QMetaObject.connectSlotsByName(MainWindowII)


    def retranslateUi(self, MainWindowII):
        _translate = QtCore.QCoreApplication.translate
        MainWindowII.setWindowTitle(_translate("MainWindowII", "Txt"))
        self.pushButton.setText(_translate("MainWindowII", "Картинка"))
        self.pushButton_2.setText(_translate("MainWindowII", "Сохранить"))
