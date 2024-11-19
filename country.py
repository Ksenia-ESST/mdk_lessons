from PyQt5 import QtWidgets
import main

d = {}
d[0] = 'Канберра'
d[1] = 'Бразилиа'
d[2] = 'Ханой'
d[3] = 'Нью-Дели'
d[4] = 'Астана'
d[5] = 'Оттава'
d[6] = 'Пекин'
d[7] = 'Монако'
d[8] = 'Абу-Даби'
d[9] = 'Исламбад'
d[10] = 'Дамаск'
d[11] = 'Вашингтон'
d[12] = 'Анкара'
d[13] = 'Берн'
d[14] = 'Мадрид'
d[15] = 'Осло'
d[16] = 'Хельсинки'
class mywindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.currentIndexChanged.connect(self.user)

    def user(self):
        self.ui.label.setText(str(d[self.ui.comboBox.currentIndex()]))    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())