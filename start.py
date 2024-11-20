from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.push.clicked.connect(self.checker)
        self.ui.clear.clicked.connect(self.clear)

    def checker(self):
       
            if self.ui.check.isChecked():
                self.ui.label.setText("Hello!")
            if self.ui.check.isChecked and self.ui.check2.isChecked():
                self.ui.label.setText("Bonjour!")
            if self.ui.check2.isChecked():
               self.ui.label2.setText("Ciao!")
            if self.ui.check.isChecked and self.ui.check2.isChecked and self.ui.check3.isChecked():
                self.ui.label.setText("Привет!")
                self.ui.label2.setText("Привет!")
                self.ui.label3.setText("Привет!")
            else:
                QtWidgets.QMessageBox.critical(window, 'Invalid choose', 'выберите любой пункт', buttons=QtWidgets.QMessageBox.Ok, defaultButton=QtWidgets.QMessageBox.Ok)
    
    def clear(self):
        self.ui.check.setChecked(False)
        self.ui.check2.setChecked(False)
        self.ui.check3.setChecked(False)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())