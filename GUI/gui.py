import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QFileDialog, QLabel
from keras.utils.image_dataset import load_image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
import extract_images_from_pickle as extract
import params

model = load_model(params.model_path)

labelscifar10 = extract.label_cifar10()
labelscifar10 = [x.decode('utf-8') for x in labelscifar10]
labelscifar100 = extract.label_cifar100()
labelscifar100 = [x.decode('utf-8') for x in labelscifar100]
labelscifar100_chosen=[labelscifar100[x] for x in params.chosen_label]
labels=labelscifar10+[None]+labelscifar100_chosen


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
        img=self.load_image(path)
        self.predict_image(img)
    def predict_image(self,img):
        predict_x = model.predict(img)
        classes_x = np.argmax(predict_x, axis=1)
        self.label.setText("predict: " + labels[classes_x[0]])


    def load_image(self,filename):
        print("load_image")
        img = load_img(filename, target_size=(32, 32))
        img = img_to_array(img)
        img = img.reshape(1, 32, 32, 3)
        img = img.astype('float32')
        img = img / 255.0
        return img


if __name__ == "__main__":
    print(labels)
    #model = load_model(r"D:\bootcamp\AMAT\project\keras_cifar10_trained_model_1A.h5")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
