from PyQt5 import QtWidgets
import main, main2

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open)

    def open(self):
        vt.show()

class VtoroeWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open2)

    def open2(self):
        a= float(self.ui.lineEdit.text())
        window.ui.label.setText(str(a+(a*0.15)))
        vt.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    vt = VtoroeWindow()
    window.show()
    sys.exit(app.exec_())