from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLabel, QComboBox, QMessageBox

from DATA import extract_images_from_pickle as extract, add_our_img
from MODEL import model_predict
from GUI import take_picture
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication
import sys

font = QtGui.QFont()
font.setFamily("Microsoft YaHei UI")
font.setPointSize(10)
font.setWeight(60)

class add_image(QWidget):
    def __init__(self, parent=None):
        super(add_image, self).__init__(parent)
        self.pred = QPushButton("predict-image", self)
        self.pred.move(0, 0)
        self.pred.setStyleSheet("height: 20;width:250;background-color: rgb(240,240,240);")
        self.pred.setFont(QtGui.QFont(font))

        self.add = QPushButton('add-image', self)
        self.add.move(250, 0)
        self.add.setStyleSheet("height: 20;width:250;background-color: rgb(200,200, 200);")
        self.add.setFont(QtGui.QFont(font))


        self.browse=QPushButton('browse-image',self)
        self.browse.clicked.connect(self.show_browse)
        self.browse.setGeometry(QtCore.QRect(50, 75, 400, 45))
        self.browse.setStyleSheet("background-color: rgb(190,250, 250);")
        self.browse.setFont(QtGui.QFont(font))
#
        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(50, 150, 400, 400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.setStyleSheet("background-color: rgb(250,250, 250);border: 1px solid black;")
        self.label_combo= QLabel(self)
        self.label_combo.setGeometry(QtCore.QRect(50, 570, 130, 30))
        self.label_combo.setText("choose the label: ")
        font1=font
        font1.setPointSize(9)
        self.label_combo.setFont(QtGui.QFont(font1))

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(180, 570, 270, 30)#200, 150, 120, 30)
        self.combo_box.addItems(extract.get_labels_name())
        self.combo_box.setFont(QtGui.QFont(font1))
        self.save = QPushButton('save-image-in-test', self)
        self.save.clicked.connect(self.save_image)
        self.save.setGeometry(QtCore.QRect(50, 640, 400, 45))
        self.save.setStyleSheet("background-color: rgb(190,250, 250);")

        self.save.setFont(QtGui.QFont(font))

        # self.acc_our=QLabel(self)
        # self.acc_our.setGeometry(QtCore.QRect(50, 630, 450, 30))
        # self.acc_our.setText("accuracy of our images: ")
        # self.acc_our.setStyleSheet("background-color: rgb(230,250, 250);border: 1px solid black;")
        # self.acc_our.setAlignment(QtCore.Qt.AlignCenter)

        self.image_path=""
        self.image_name=""
        #self.combo_box.activated[str].connect(self.combo_changed)
    def show_browse(self):
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.*)')[0]
        if not path:
            return
        self.photo.setPixmap(QtGui.QPixmap(path))
        self.image_name = path[path.rfind("/")+1:]
        self.image_path=path

    def save_image(self):
        label=self.combo_box.currentText()
        print(label)
        if not self.image_path=="":
            add_our_img.save_single_image(label,self.image_path,self.image_name)
            QMessageBox.about(self, "massage","the image saved!")
        else:
            QMessageBox.about(self, "massage", "the image did not save!\n please browse image")
        # acc=model_predict.
        # self.acc_our.setText(self.acc_our.text()+)

class predict_image(QWidget):
    def __init__(self, parent=None):
        super(predict_image, self).__init__(parent)
        self.pred = QPushButton("predict-image", self)
        self.pred.move(0, 0)
        self.pred.setStyleSheet("height: 20;width:250;background-color: rgb(200, 200,200)")
        self.pred.setFont(QtGui.QFont(font))
        self.add = QPushButton('add-image', self)
        self.add.move(250, 0)
        self.add.setStyleSheet("height: 20;width:250;background-color: rgb(240,240, 240)")
        self.add.setFont(QtGui.QFont(font))

        self.browse=QPushButton('browse-image',self)
        self.browse.clicked.connect(self.show_browse)
        self.browse.setGeometry(QtCore.QRect(50, 75, 180, 45))
        self.browse.setStyleSheet("background-color: rgb(190,250, 250);")
        self.browse.setFont(QtGui.QFont(font))

        self.take_picture = QPushButton("take-picture",self)
        self.take_picture.setGeometry(QtCore.QRect(260, 75, 190, 45))
        self.take_picture.setStyleSheet("background-color: rgb(180,250, 250);")
        self.take_picture.clicked.connect(self.show_take_picture)
        self.take_picture.setFont(QtGui.QFont(font))
        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(50, 150, 400, 400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        #self.photo.setScaledContents(False)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.setStyleSheet("background-color: rgb(250,250, 250);border: 1px solid black;")

        self.predict= QLabel(self)
        self.predict.setGeometry(QtCore.QRect(50, 580, 400, 45))
        self.predict.setText("prediction")
        self.predict.setStyleSheet("background-color: rgb(230,250, 250);border: 1px solid black;")
        self.predict.setAlignment(QtCore.Qt.AlignCenter)
        self.predict.setFont(QtGui.QFont(font))

        self.predict_data = QLabel(self)
        self.predict_data.setGeometry(QtCore.QRect(50, 630, 400, 45))
        self.predict_data.setText("predict_data")
        self.predict_data.setStyleSheet("background-color: rgb(230,250, 250);border: 1px solid black;")
        self.predict_data.setAlignment(QtCore.Qt.AlignCenter)
        self.predict_data.setFont(QtGui.QFont(font))

    def show_browse(self):
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.*)')[0]
        if not path:
            return
        self.photo.setPixmap(QtGui.QPixmap(path))
        img= model_predict.load_image(path)
        self.show_predict_on_labels(img)

    def show_take_picture(self):
        path= take_picture.capture()
        if not path:
            return
        self.photo.setPixmap(QtGui.QPixmap(path))
        img = model_predict.load_image(path)
        self.show_predict_on_labels(img)
    def show_predict_on_labels(self,img):
        pred1, prob1, pred2, prob2 = model_predict.predict_image(img)
        print(type(prob1))
        self.predict_data.setText(f"first place: {pred1} {str(round(prob1, 2))}%\nsecond place: {pred2} {str(round(prob2, 2))}%")
        self.predict.setText("classified as " + pred1)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(500, 750)
        self.start_predict_window()


    def start_predict_window(self):
        self.predict_image = predict_image(self)
        self.setWindowTitle("classification project")
        self.setCentralWidget(self.predict_image)
        self.predict_image.add.clicked.connect(self.start_add_window)
        self.show()


    def start_add_window(self):
        self.add_image = add_image(self)
        self.setWindowTitle("classification project")
        self.setCentralWidget(self.add_image)
        self.add_image.pred.clicked.connect(self.start_predict_window)
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())