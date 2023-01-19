# importing PyQt5 for gui

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PIL import ImageTk, Image
import assistant as sp


def assistant():
    sp.TextToSpeak("")
    sp.TextToSpeak("")
    sp.TextToSpeak("")
    # sp.welcomeSpeak()
    sp.assistant()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        # setting geometry
        self.setGeometry(100, 100, 400, 300)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.showFullScreen()
        assistant()


    # method for widgets
    def UiComponents(self):
        # creating label
        label = QLabel(self)
        # setting geometry to label
        label.setGeometry(0, 0, 600, 400)
        # loading image
        pixmap = QPixmap('res/images/asst-bg.jpg')
        # adding image to label
        label.setPixmap(pixmap)
        # Optional, resize label to image size
        label.resize(pixmap.width(), pixmap.height())
        # opening window in maximized size


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()
    # start the app
    sys.exit(App.exec())

