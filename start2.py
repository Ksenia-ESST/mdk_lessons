from PyQt5 import QtWidgets
import main2

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main2.Ui_Form()
        self.ui.setupUi(self)

        self.ui.button1.clicked.connect(self.sum)
        self.ui.button2.clicked.connect(self.clear)

    def sum(self):
        try:
            a = float(self.ui.line.text())
            b = float(self.ui.line2.text())
            e = a * b

            if self.ui.check.isChecked():
                e *= 2
            if self.ui.check2.isChecked():
                e /= 2
            if self.ui.check3.isChecked():
                e *= e

            self.ui.line3.setText(f'Площадь: {e}')
        except ValueError:
            self.ui.line3.setText('Введите корректные числа!')

    def clear(self):
        self.ui.line.clear()
        self.ui.line2.clear()
        self.ui.line3.clear()
        self.ui.check.setChecked(False)
        self.ui.check2.setChecked(False)
        self.ui.check3.setChecked(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())