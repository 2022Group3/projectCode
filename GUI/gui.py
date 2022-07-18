import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFileDialog, QLabel

import extract_images_from_pickle as extract
import params
import model_predict


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(50, 130,400,400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.label= QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 600, 400, 45))
        self.label.setText("prediction")

        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(50, 50, 400, 45))
        self.browse.setObjectName("browse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse.clicked.connect(self.show_browse)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse.setText(_translate("MainWindow", "browse"))

    def show_browse(self):
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.png)')[0]
        self.photo.setPixmap(QtGui.QPixmap(path))
        img=model_predict.load_image(path)
        predict=model_predict.predict_image(img)
        self.label.setText("predict: " + predict)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
