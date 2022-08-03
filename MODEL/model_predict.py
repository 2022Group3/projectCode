import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import img_to_array
from keras.models import load_model
from DATA import extract_images_from_pickle as extract
import params

model = load_model(params.model_path)
labels = extract.get_labels_name()


def load_image(filename: str) -> list[list[float]]:
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = img.reshape(1, 32, 32, 3)
    img = img.astype('float32')
    img = img / 255.0
    return img


def predict_image(img: list[list[float]]) -> tuple[str, float, str, float, bool, bool]:
    """
    get the prediction for an image, and how much the model is confident
    :param img: image you want to predict
    :return:
    """
    predict_x = model.predict(img, verbose=0)
    classes_x1 = np.argmax(predict_x, axis=1)
    first_prob = (predict_x[0])[classes_x1][0] * 100
    predict_x[0][classes_x1] = 0.0
    classes_x2 = np.argmax(predict_x, axis=1)
    second_prob = (predict_x[0])[classes_x2][0] * 100
    out_of_distribution = False
    confidence = True
    # dif = first_prob - second_prob
    # if first_prob + second_prob < 90 and first_prob < 50:
    #     out_of_distribution = True
    # elif dif < 70:
    #     confidance = False

    # if dif < 30 and first_prob < 40:
    #     out_of_distribution = True
    # elif dif < 45:
    #     confidance = False

    # if first_prob < 20:
    #     out_of_distribution = True
    # elif first_prob >= 20 and first_prob < 70:
    #     confidance = False
    #
    # if first_prob + second_prob < 80:
    #     out_of_distribution = True
    if first_prob + second_prob < 70:
        out_of_distribution = True
    if second_prob != 0 and first_prob / second_prob < 6:
        confidence = False

    return labels[classes_x1[0]], first_prob, labels[classes_x2[0]], second_prob, out_of_distribution, confidence
