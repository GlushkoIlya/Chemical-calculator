import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QMainWindow, QCheckBox, \
    QComboBox, QFileDialog


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Химический калькулятор')
        self.cbox.activated[str].connect(self.Next)

    def Next(self, text):
        if text == "Масса вещества":
            self.nextWindow = AtomnayaMassa()
            self.nextWindow.show()


class AtomnayaMassa(QWidget):
    def __init__(self):
        print(4)
        super().__init__()
        uic.loadUi('AM.ui', self)
        self.setWindowTitle("Масса вещества")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
