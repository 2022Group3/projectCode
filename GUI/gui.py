
import logging
import os
from ctypes.wintypes import RGB
from PIL import ImageOps, Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QPixmap, QMouseEvent, QIcon
from PyQt5.QtWidgets import QFileDialog, QLabel, QComboBox, QMessageBox, QRubberBand
from PyQt5.QtWidgets import *

from DATA import extract_images_from_pickle as extract, add_our_img
from MODEL import model_predict
from GUI import take_picture
from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication
import sys
import params

font = QtGui.QFont()
font.setFamily("my family")
font.setPointSize(11)
font.setWeight(80)
font.setBold(False)

font1 = QtGui.QFont()
font1.setFamily("my family")
font1.setPointSize(11)
font1.setWeight(80)
font1.setBold(False)

fontb = QtGui.QFont()
fontb.setFamily("my family")
fontb.setPointSize(11)
fontb.setWeight(80)
fontb.setBold(True)


class image(QLabel):
    def __init__(self, parent=None):
        super(image, self).__init__(parent)
        self.current_rubber_band = None
        self.origin_point = None

    def mousePressEvent(self, mouse_event: QMouseEvent) -> None:
        logging.info("mousePressEvent")
        self.origin_point = mouse_event.pos()
        self.current_rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.current_rubber_band.setGeometry(QRect(self.origin_point, QSize()))
        self.current_rubber_band.show()

    def mouseMoveEvent(self, mouse_event: QMouseEvent) -> None:
        logging.info("mouseMoveEvent")
        self.current_rubber_band.setGeometry(QRect(self.origin_point, mouse_event.pos()).normalized())

    def mouseReleaseEvent(self, mouse_event: QMouseEvent) -> None:
        logging.info("mouseReleaseEvent")
        self.current_rubber_band.hide()
        current_rect: QRect = self.current_rubber_band.geometry()
        self.current_rubber_band.deleteLater()
        print(current_rect)
        crop_pixmap: QPixmap = self.pixmap().copy(current_rect)
        crop_pixmap.save(params.crop_img_path)
        print("a")
        window.predict_image.show_image(params.crop_img_path)


class add_image(QWidget):
    def __init__(self, parent=None):
        super(add_image, self).__init__(parent)

        self.browse = QPushButton('browse-an-image', self)
        self.browse.clicked.connect(self.show_browse)
        self.browse.setGeometry(QtCore.QRect(30, 45, 410, 45))
        self.browse.setStyleSheet("background-color: rgb(190,230, 230);")
        self.browse.setFont(QtGui.QFont(fontb))

        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(30, 120, 410, 410))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.setStyleSheet("background-color: rgb(250,250, 250);border: 1px solid black;")

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(30, 550, 410, 30)
        self.combo_box.addItems(["choose label:"] + extract.get_labels_name())
        self.combo_box.setCurrentText("choose label:")
        self.combo_box.setFont(QtGui.QFont(font))

        self.save = QPushButton('save-image-in-test', self)
        self.save.clicked.connect(self.save_image)
        self.save.setGeometry(QtCore.QRect(30, 610, 410, 45))
        self.save.setStyleSheet("background-color: rgb(190,230, 230);")
        self.save.setFont(QtGui.QFont(fontb))
        self.save.setEnabled(False)
        self.image_path = ""
        self.image_name = ""

    def show_browse(self) -> None:
        """
        upload an image from the computer and show it.
        :return: None
        """
        logging.info("show_browse")
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.*)')[0]
        if not path:
            return
        self.save.setEnabled(True)
        self.show_image(path)
        self.image_name = path[path.rfind("/") + 1:]
        self.image_path = path

    def show_image(self, img_path: os.path) -> None:
        """
        display an image in the grid
        :param img_path:
        :return:
        """
        logging.info("show_image: "+img_path)
        self.convert_image_to_square(img_path)
        self.photo.setPixmap(QtGui.QPixmap(params.seq_img_path))

    def convert_image_to_square(self, image_path: os.path) -> None:
        """
        convert every image to square image
        :param image_path: the image path to square
        :return: None
        """
        logging.info("convert_image_to_square")
        image = Image.open(image_path)
        h = image.height
        w = image.width
        border_top = 0
        border_bottom = 0
        border_right = 0
        border_left = 0
        if h < w:
            border_top = (w - h) // 2
            border_bottom = border_top
        else:
            border_left = (h - w) // 2
            border_right = border_left
        print("1")
        border = (border_right, border_top, border_left, border_bottom)
        image_bord = ImageOps.expand(image, border=border, fill=RGB(240, 240, 240))
        image_res = image.resize((400, 400))
        image_res.save(params.seq_img_path)

    def save_image(self) -> None:
        """
        save image in the test
        :return: None
        """
        label = self.combo_box.currentText()
        print(label)
        if not self.image_path == "":
            add_our_img.save_single_image(label, params.seq_img_path, self.image_name)
            add_our_img.save_image_to_analyze(label, self.image_path, self.image_name)
            QMessageBox.about(self, "massage", "the image saved!")


class predict_image(QWidget):
    def __init__(self, parent=None):
        super(predict_image, self).__init__(parent)
        self.browse = QPushButton('Browse-an-image', self)
        self.browse.clicked.connect(self.show_browse)
        self.browse.setGeometry(QtCore.QRect(30, 40, 200, 45))
        self.browse.setStyleSheet("background-color: rgb(190,230, 230);")
        self.browse.setFont(QtGui.QFont(fontb))

        self.take_picture = QPushButton("Take-a-picture", self)
        self.take_picture.setGeometry(QtCore.QRect(240, 40, 200, 45))
        self.take_picture.setStyleSheet("background-color: rgb(190,230, 230);")
        self.take_picture.clicked.connect(self.show_take_picture)
        self.take_picture.setFont(QtGui.QFont(fontb))

        self.photo = image(self)  # QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(30, 110, 410, 410))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.photo.setStyleSheet("background-color: rgb(250,250, 250);border: 1px solid black;")

        self.reset_image = QPushButton(self)
        self.reset_image.clicked.connect(self.return_to_the_base_img)
        self.reset_image.setGeometry(QtCore.QRect(31, 111, 50, 50))
        self.reset_image.setStyleSheet("background-color: transparent;")
        self.reset_image.setIcon(QIcon(params.icon_path))
        self.reset_image.setIconSize(QSize(50, 50))

        self.predict_button = QPushButton("PREDICT", self)
        self.predict_button.setGeometry(135, 505, 200, 45)
        self.predict_button.setStyleSheet("background-color: rgb(200,0, 0);border: 1px solid black;")
        self.predict_button.setFont(QtGui.QFont(fontb))
        self.predict_button.clicked.connect(self.show_predict_on_labels)
        self.predict_button.setEnabled(False)

        self.predict = QLabel(self)
        self.predict.setGeometry(QtCore.QRect(30, 570, 410, 45))
        self.predict.setStyleSheet("background-color: rgb(230,250, 250);border: 1px solid black;")
        self.predict.setAlignment(QtCore.Qt.AlignCenter)
        self.predict.setFont(QtGui.QFont(fontb))

        self.predict_data = QLabel(self)
        self.predict_data.setGeometry(QtCore.QRect(30, 625, 410, 50))
        self.predict_data.setStyleSheet("background-color: rgb(230,250, 250);border: 1px solid black;")
        self.predict_data.setAlignment(QtCore.Qt.AlignCenter)
        self.predict_data.setFont(QtGui.QFont(font))
        self.reset_predicts_labels()
        self.image_path = ""
        if os.path.exists(params.base_img_path):
            os.remove(params.base_img_path)
        if os.path.exists(params.seq_img_path):
            os.remove(params.seq_img_path)
        if os.path.exists(params.crop_img_path):
            os.remove(params.crop_img_path)
        if os.path.exists(params.cam_img_path):
            os.remove(params.cam_img_path)

    def not_sure_alert(self, out_of_distribution: bool, confidence: bool) -> None:
        """

        :param out_of_distribution: is the model doesn't recognize the image class
        :param confidence: is the model debate on it predict
        :return: None
        """
        # label = self.combo_box.currentText()
        if out_of_distribution:
            QMessageBox.about(self, "warning",
                              "Hummm...🤔 \n I'm not sure about that one \n Is your image out of distribution? ")
        elif not confidence:
            QMessageBox.about(self, "warning", "Hummm...🤔 I'm debating \n Try again!")

    def show_browse(self) -> None:
        """
        upload an image from the computer and show it.
        :return: None
        """
        logging.info("show_browse")
        path = QFileDialog.getOpenFileName(None, 'Load motor', '', 'Motor Files (*.png)')[0]
        if path:
            self.predict_button.setEnabled(True)
            image = Image.open(path)
            image.save(params.crop_img_path)
            image.save(params.base_img_path)
            self.show_image(path)

    def show_image(self, img_path: os.path) -> None:
        """
        display an image in the grid
        :param img_path:
        :return:
        """
        logging.info("show_image")
        if os.path.exists(img_path):
            self.reset_predicts_labels()
            self.convert_image_to_square(img_path)
            self.photo.setPixmap(QtGui.QPixmap(params.seq_img_path))
            self.image_path = params.seq_img_path

    def convert_image_to_square(self, image_path: os.path) -> None:
        """
        convert every image to square image
        :param image_path: the image path to square
        :return: None
        """
        logging.info("convert_image_to_square")
        image = Image.open(image_path)
        print(image_path)
        h = image.height
        w = image.width
        border_top = 0
        border_bottom = 0
        border_right = 0
        border_left = 0
        if h < w:
            border_top = (w - h) // 2
            border_bottom = border_top
        else:
            border_left = (h - w) // 2
            border_right = border_left
        border = (border_right, border_top, border_left, border_bottom)
        image_bord = ImageOps.expand(image, border=border, fill=RGB(240, 240, 240))
        image_res = image_bord.resize((410, 410))
        image_res.save(params.seq_img_path)

    def show_take_picture(self) -> None:
        """
        display an image in the grid
        :return: None
        """
        logging.info("show_take_picture")
        path = take_picture.capture()
        if path:
            self.predict_button.setEnabled(True)
            image = Image.open(path)
            image.save(params.base_img_path)
            image.save(params.crop_img_path)
            self.show_image(path)
            self.image_path = path

    def reset_predicts_labels(self) -> None:
        """
        reset the  model prediction label's
        :return:None
        """
        logging.info("reset_predicts_labels")
        self.predict.setText("The prediction")
        self.predict_data.setText("more information")

    def show_predict_on_labels(self) -> None:
        """
        show predict of the display image in the predict lables
        :return: None
        """
        logging.info("show_predict_on_labels")
        img = model_predict.load_image(params.crop_img_path)
        pred1, prob1, pred2, prob2, out_of_distribution, confidance = model_predict.predict_image(img)
        self.predict.setText("classified as " + pred1)
        self.predict_data.setText(
            f"first place: {pred1} {str(round(prob1, 2))}%\nsecond place: {pred2} {str(round(prob2, 2))}%")
        self.predict.setText("classified as " + pred1)
        self.not_sure_alert(out_of_distribution, confidance)

    def return_to_the_base_img(self) -> None:
        """
        return to the image base and show it
        :return:None
        """
        logging.info("return_to_the_base_img")
        if os.path.exists(params.base_img_path):
            self.show_image(params.base_img_path)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(500, 750)
        layout = QGridLayout()
        self.setLayout(layout)
        self.predict_image = predict_image(self)
        self.add_image = add_image(self)
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.predict_image, "      Predict-an-image      ")
        self.tabWidget.addTab(self.add_image, "        Add-an-image        ")
        self.tabWidget.setFont(QtGui.QFont(font1))
        self.setWindowTitle("classification project Group3")
        layout.addWidget(self.tabWidget)


app = QApplication(sys.argv)
window = MainWindow()