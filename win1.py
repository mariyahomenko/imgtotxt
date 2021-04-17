from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("QMainWindow {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"stop:0 white, stop: 0.4 rgba(146,146,146,1),\n"
"stop:1 rgb(242,242,255))\n"
"}\n"
"\n"
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
"QLabel {\n"
"background-color: #c6c6c6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #7bb87b;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 700, 500))
        self.label.setFont(QtGui.QFont('Georgia', 16))
        self.label.setText("    Чтобы загрузить картинку, нажмите на кнопку 'Открыть'\n"
                           "    и выберите файл с картинкой, с которой хотите получить текст.\n"
                           "    Не переживайте, если она видоизменилась. Программа будет\n"
                           "    работать с оригинальным изображением, а не с отображаемым.\n"
                           "    Нажмите на кнопку 'Текст' и проверьте результат.\n"
                           "    При необходимости, сверяясь с картинкой, исправьте недочеты,\n"
                           "    затем нажмите на кнопку 'Сохранить'.\n"
                           "\n"
                           "    По умолчанию распознается русский язык.\n"
                           "\n"
                           "    Изображение должно иметь файловое имя на латинице.")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 550, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 550, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filename = None
        self.tmp = None
        self.tmptxt = None
        self.num = 0
        self.txt = None
        self.numopen = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Img"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))
        self.pushButton_2.setText(_translate("MainWindow", "Текст"))
