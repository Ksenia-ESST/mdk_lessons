from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        self.ui.push.clicked.connect(self.start)
        self.ui.push1.clicked.connect(self.dalshe1)
        self.ui.push2.clicked.connect(self.dalshe2)
        self.ui.push3.clicked.connect(self.dalshe3)
        self.ui.push4.clicked.connect(self.dalshe4)
        self.ui.push5.clicked.connect(self.dalshe5)
        self.ui.push6.clicked.connect(self.dalshe6)
        self.ui.push7.clicked.connect(self.dom)

    def start(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def dalshe1(self):
        if self.ui.rad111.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def dalshe2(self):
        if self.ui.rad222.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def dalshe3(self):
        if self.ui.rad333.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def dalshe4(self):
        if self.ui.rad444.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(5)
        
    def dalshe5(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        if self.ui.rad555.isChecked():
            self.a += 1
        
    def dalshe6(self):
        if self.ui.rad666.isChecked():
            self.a += 1
        self.ui.stackedWidget.setCurrentIndex(7)

        ocenka = {
            0 : 2,
            1 : 2,
            2 : 2,
            3 : 3,
            4 : 4,
            5 : 5,
        }
        self.ui.labe77.setText(f"{self.a}")
        self.ui.lab88.setText(f"{ocenka[self.a]}")

    def dom(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        self.a = 0
        for i in range(1,10):
            btn = getattr(self.ui, "rad{}".format(i))
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())