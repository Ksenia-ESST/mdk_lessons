from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.line2.textChanged.connect(self.deq)
        self.ui.line.textChanged.connect(self.deq)
        self.ui.push.clicked.connect(self.dan)  

    def deq(self):
        try:    
            a = int(self.ui.line2.text())
            b = int(self.ui.line.text())
            c = a*b
            if a is not None and b  is not None:
                self.ui.label_2.setText(f"Амортизация налогового учета = {str(c)}")
        except:
            self.ui.label_2.setText(f"Амортизация налогового учета = ")
    def dan(self):
        number = self.ui.line3.text()
        avtor = self.ui.line4.text()
        date = self.ui.line5.text()
        cvv = self.ui.line6.text()
        self.ui.label3_2.setText(f"Данные: {number} {avtor} {date} {cvv}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())