from PyQt5 import QtWidgets
import main1, main2, main3

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main1.Ui_Form()
        self.ui.setupUi(self) 
        self.ui.push.clicked.connect(self.open)
        self.ui.push2.clicked.connect(self.closp)

# class Avto(QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.ui = main1.Ui_Form()
#         self.ui.setupUi(self)
       
    def open(self):
        if self.ui.line.text() == "admin" and self.ui.line2.text() == "admin":
            window.show()
            # main2.close()
            th.show()
        elif self.ui.line.text() == "":
            self.ui.label.setText("Введите логин")
        elif self.ui.line2.text() == "":
            self.ui.label.setText("Введите пароль")
            th.show()
        else:
            self.ui.label.setText("Неправильно")
            self.ui.line.clear()
            self.ui.line2.clear()
            tw.show()

    def closp(self):
        self.ui.line.clear()
        self.ui.line2.clear()
        # main2.close()

class TwoWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open2)

    def open2():
        window.show()

class ThreeiWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main3.Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    tw = TwoWindow()
    th = ThreeiWindow()
    window.show()
    sys.exit(app.exec_())