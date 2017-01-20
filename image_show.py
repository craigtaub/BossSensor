# -*- coding: utf-8 -*-
#'s_pycharm.jpg'):
import sys

from PyQt4 import QtGui


def show_image(image_path='./images_to_display/das_dash.jpg'):
    app = QtGui.QApplication(sys.argv)
    pixmap = QtGui.QPixmap(image_path)
    screen = QtGui.QLabel()
    screen.setPixmap(pixmap)
    screen.showFullScreen()
    # sys.exit(app.exec_()) DONT EXIT


if __name__ == '__main__':
    show_image()
