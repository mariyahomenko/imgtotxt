from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import sys
from win1 import Ui_MainWindow
from win2 import Ui_MainWindowII
from PIL import Image
import pytesseract

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
MainWindowII = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
uiII = Ui_MainWindowII()

ui.setupUi(MainWindow)
uiII.setupUi(MainWindowII)


# Прячу кнопку "Текст"
ui.pushButton_2.hide()

MainWindow.show()


# Вызывается кнопкой "Открыть"
def numopen():
    ui.numopen += 1
    if ui.numopen == 1:
        loadimage()

    # Обнуляю глобальные переменные при каждом нажатии
    else:
        ui.filename = None
        ui.tmp = None
        ui.tmptxt = None
        ui.num = 0
        ui.txt = None

        loadimage()


# Вызывается функцией numopen
def loadimage():
    try:
        ui.filename = QFileDialog.getOpenFileName(filter='Image (*.*)')[0]
        img = cv2.imread(ui.filename)

        if img is None:

            # На случай, если картинка загружается повторно, но с негативным сценарием
            ui.pushButton_2.hide()
            ui.label.setText('Изображение не загружено')
        else:
            # Передаю изображение в функцию обработки и вызываю ее
            set(img)
    except:
        ui.pushButton_2.hide()
        ui.label.setText('Ошибка при загрузке файла')


# Вызывается функцией loadimage
def set(img):
    try:
        # Записываю картинку для дальнейшего использования
        ui.tmp = img
        #img = cv2.resize(img, (800, 565))
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)

        # Вывожу обработанную картинку в окно и открываю кнопку "Текст"
        ui.label.setPixmap(QtGui.QPixmap.fromImage(img))
        ui.pushButton_2.show()
    except:
        ui.label.setText('Ошибка при выводе изображения на экран.\n'
                         'Но продолжайте')
        ui.pushButton_2.show()


# Вызывается кнопкой "Текст"
def num():
    ui.num += 1
    if ui.num == 1:

        # Тессерактовая обработка
        txt()
    else:
        # Редактирование созданного текста пользователем
        edit()


# Вызывается функцией num в том случае, если кнопка "Текст" нажата впервые
def txt():
    try:
        MainWindow.hide()
        MainWindowII.show()

        img = ui.filename
        text = pytesseract.image_to_string(Image.open(img), lang = 'rus')

        # Сохраняю результат обработки в глобальную переменную
        ui.tmptxt = text

        # Очистка на случай, если картинка загружена не впервые
        uiII.textEdit.clear()
        uiII.textEdit.insertPlainText(ui.tmptxt)

        # Начинаю кэшировать текстовое поле, чтобы не запутаться
        ui.txt = uiII.textEdit.toPlainText()

    except:
        ui.label.setText('Ошибка при попытке перевести изображение в текст')


# Вызывается функцией num в случае, если явно происходит редактирование текста
def edit():
    MainWindow.hide()
    MainWindowII.show()

    # Заполняю текстовое поле содержимым глобальной переменной
    # Очистка, чтобы текст не дублировался при каждом вызове
    uiII.textEdit.clear()
    uiII.textEdit.insertPlainText(ui.txt)


# Вызывается кнопкой "Сохранить"
def save():
    try:
        x = ui.filename
        x = x[:-3] + 'txt'
        y = ui.txt
        f = open(x, 'w')
        f.write(y)
        f.close()

        # Возвращаю первое окно с сообщением об успешном сохранении и прячу кнопку "Текст"
        MainWindowII.hide()
        ui.pushButton_2.hide()
        MainWindow.show()
        ui.label.setText(f'Сохранено как: {x}')
    except:
        MainWindowII.hide()
        ui.pushButton_2.hide()
        MainWindow.show()
        ui.label.setText('Ошибка при создании текстового документа')


# Вызывается кнопкой "Картинка" при сравнении текста с изображением
def pctr():
    ui.txt = uiII.textEdit.toPlainText()
    MainWindowII.hide()
    MainWindow.show()
    img = ui.tmp
    #img = cv2.resize(img, (800, 565))
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
    ui.label.setPixmap(QtGui.QPixmap.fromImage(img))


# Кнопка "Открыть"
ui.pushButton.clicked.connect(lambda: numopen())

# Кнопка "Текст"
ui.pushButton_2.clicked.connect(lambda: num())

# Кнопка "Картинка"
uiII.pushButton.clicked.connect(lambda: pctr())

# Кнопка "Сохранить"
uiII.pushButton_2.clicked.connect(lambda: save())


sys.exit(app.exec_())
