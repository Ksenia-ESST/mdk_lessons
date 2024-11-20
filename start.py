from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)

        self.ui.push1.clicked.connect(self.Text)
        self.ui.push2.clicked.connect(self.Int)
        self.ui.push3.clicked.connect(self.Double)
        self.ui.push4.clicked.connect(self.Item)

    def Text(self):
        text, ok = QtWidgets.QInputDialog.getText(window, "Заголовок", "Подсказка", echo = 0 )
        if ok:
            self.ui.line1.setText(str(text))

    def Int(self):
        c_chislo, ok = QtWidgets.QInputDialog.getInt(window, "Заголовок", "Подсказка", min = 0, max = 10, step = 1 )
        if ok:
            self.ui.line1.setText(str(c_chislo))

    def Double(self):
        v_chislo, ok = QtWidgets.QInputDialog.getDouble(window, "Заголовок", "Подсказка", min = 0, max = 10, decimals = 3 )
        if ok:
            self.ui.line1.setText(str(v_chislo))

    def Item(self):
        item, ok = QtWidgets.QInputDialog.getItem(window, "Заголовок", "Подсказка", ["Пункт 1", "Пункт 2", "Пункт 3"], current = 0, editable = False)
        if ok:
            self.ui.line1.setText(str(item))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())