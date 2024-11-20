from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action.triggered.connect(app.quit)
        self.ui.action_2.triggered.connect(self.avtor)
        self.ui.actionOpen_file.triggered.connect(self.open_file)
        

    def avtor(self):
        self.ui.label.setText("ИП 24-26Б")

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                self.ui.textEdit.setPlainText(content)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())