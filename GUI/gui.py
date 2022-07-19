import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFileDialog, QLabel

import extract_images_from_pickle as extract
import params
import model_predict
import take_picture

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(50, 130,400,400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.setStyleSheet("background-color: rgb(250,250, 250);border: 1px solid black;")
        self.predict= QtWidgets.QLabel(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(50, 580, 400, 45))
        self.predict.setAlignment(QtCore.Qt.AlignCenter)
        self.predict.setText("prediction")
        self.predict.setStyleSheet("background-color: rgb(180,250, 250);border: 1px solid black;")
        self.predict_data = QtWidgets.QLabel(self.centralwidget)
        self.predict_data.setGeometry(QtCore.QRect(50, 630, 400, 45))
        self.predict_data.setAlignment(QtCore.Qt.AlignCenter)
        self.predict_data.setText("predict_data")
        self.predict_data.setStyleSheet("background-color: rgb(180,250, 250);border: 1px solid black;")
        myFont = QtGui.QFont()
        myFont.setBold(True)
        self.predict.setFont(myFont)
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(50, 50, 180, 45))
        self.browse.setObjectName("browse")
        self.browse.setStyleSheet("background-color: rgb(180,250, 250);")
        self.take_picture = QtWidgets.QPushButton(self.centralwidget)
        self.take_picture.setGeometry(QtCore.QRect(270, 50, 180, 45))
        self.take_picture.setObjectName("take_picture")
        self.take_picture.setStyleSheet("background-color: rgb(180,250, 250);")
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
        self.take_picture.clicked.connect(self.show_take_picture)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "classification project"))
        self.browse.setText(_translate("MainWindow", "browse"))
        self.take_picture.setText(_translate("MainWindow", "take picture"))

    def show_browse(self):
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.*)')[0]
        if not path:
            return
        self.photo.setPixmap(QtGui.QPixmap(path))
        img=model_predict.load_image(path)
        self.show_predict_on_labels(img)

    def show_take_picture(self):
        path=take_picture.capture()
        if not path:
            return
        self.photo.setPixmap(QtGui.QPixmap(path))
        img = model_predict.load_image(path)
        self.show_predict_on_labels(img)
    def show_predict_on_labels(self,img):
        pred1, prob1, pred2, prob2 = model_predict.predict_image(img)
        print(type(prob1))
        self.predict_data.setText(f"first place:  {pred1}   {str(round(prob1, 2))}%\n  second place: {pred2} {str(round(prob2, 2))} %")
        self.predict.setText("classified as " + pred1)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
