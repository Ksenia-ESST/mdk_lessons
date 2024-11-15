from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(self.sum)
        self.ui.button_2.clicked.connect(self.clear)

    def sum(self):
        a = float(self.ui.line.text())
        b = float(self.ui.line_2.text())
        c = float(self.ui.line_3.text())
        d = float(self.ui.lin_4.text())
        e = a + b + c + d
        self.ui.line_5.setText(f"Сумма = {str(e)}")

    def clear(self):
        self.ui.line.clear()
        self.ui.line_2.clear()
        self.ui.line_3.clear()
        self.ui.lin_4.clear()
        self.ui.line_5.setText(f"Сумма = ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())



        
    
    