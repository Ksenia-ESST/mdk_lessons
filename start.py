from PyQt5 import QtWidgets, QtCore, QtGui
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.push.clicked.connect(self.conver)

        
        
        self.ui.line.setValidator(QtGui.QDoubleValidator())
        self.ui.line.setValidator(
            QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+[.][0-9]")))
        
        self.ui.line2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("")))

    
    
    def conver(self):
        c = 0
        a = float(self.ui.Iz.text())
        if self.ui.Km1.isChecked() and self.ui.Km2.isChecked():
            c = round(a, 2)
        if self.ui.Km1.isChecked() and self.ui.M2.isChecked():
            c = round((a * 1000), 2)
        if self.ui.Km1.isChecked() and self.ui.Sm2.isChecked():
            c = round((a * 100000), 3)


        if self.ui.M1.isChecked() and self.ui.Km2.isChecked():
            c = round((a*100), 2)
        if self.ui.M1.isChecked() and self.ui.M2.isChecked():
            c = round((a), 2)
        if self.ui.M1.isChecked() and self.ui.Sm2.isChecked():
            c = round((a / 1000), 2)

        
        if self.ui.Sm1.isChecked() and self.ui.Km2.isChecked():
            c = round((a* 100000), 3)
        if self.ui.Sm1.isChecked() and self.ui.M2.isChecked():
            c = round((a*100), 2)
        if self.ui.Sm1.isChecked() and self.ui.Sm2.isChecked():
            c = round(a, 2)

        self.ui.line2.setText(str(c))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())