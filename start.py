from PyQt5 import QtCore, QtWidgets, QtMultimedia
import main, os

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.sndEffect = QtMultimedia.QSoundEffect()
        self.ui.pushButton.clicked.connect(self.sound1)
        self.ui.pushButton_2.clicked.connect(self.sound2)

    def sound1(self):
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("net.wav"))
        self.sndEffect.setSource(fn)
        self.sndEffect.setVolume(1)
        self.sndEffect.play()

    def sound2(self):
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("2.wav"))
        self.sndEffect.setSource(fn)
        self.sndEffect.setVolume(0.5)
        self.sndEffect.play()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())