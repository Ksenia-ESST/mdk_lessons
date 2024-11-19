from PyQt5 import QtWidgets
import main

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.click.clicked.connect(self.click_me)
        self.ui.exit.clicked.connect(self.exit)
        self.ui.programm.clicked.connect(self.about_programm)
         
    def click_me(self):
        number_or_char = self.ui.input.text()
        if len(number_or_char) == 0:
            a = QtWidgets.QMessageBox.information(window, "Информация", "Вы ничего не ввели", 
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        if number_or_char == "1":
            b = QtWidgets.QMessageBox.warning(window, "Предупреждение", "Действие может быть опасным. Продолжить?", 
                                              buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                              defaultButton=QtWidgets.QMessageBox.No)
            if b == QtWidgets.QMessageBox.No:
                self.ui.input.clear()
                
        if number_or_char == "2":
            c = QtWidgets.QMessageBox.critical(window, "Критическая ошибка", "Недопустимая ошибка.Закрываю программу", 
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
            if c == QtWidgets.QMessageBox.Ok:
                sys.exit(app.quit)
        
    def exit(self):
        d = QtWidgets.QMessageBox.question(window, "Выход", "Вы действительно хотите выйти?", 
                                              buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                              defaultButton=QtWidgets.QMessageBox.No)
        if d == QtWidgets.QMessageBox.Yes:
            sys.exit(app.quit)
        
    def about_programm(self):
        e = QtWidgets.QMessageBox.about(window, "О Программе", "QMessageBox\nАвтор: Бурдина Ксения")
                                              

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())