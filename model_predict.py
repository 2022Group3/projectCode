import numpy as np
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
print(labels)

def load_image(filename):
    print("load_image")
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = img.reshape(1, 32, 32, 3)
    img = img.astype('float32')
    img = img / 255.0
    return img

def predict_image(img):
    print("predict_image")
    predict_x = model.predict(img,verbose=0)
    print(predict_x)
    classes_x1 = np.argmax(predict_x, axis=1)
    first_prob=(predict_x[0])[classes_x1][0]*100
    predict_x[0][classes_x1]=0.0
    classes_x2 = np.argmax(predict_x, axis=1)
    second_prob=(predict_x[0])[classes_x2][0]*100
    return labels[classes_x1[0]],first_prob,labels[classes_x2[0]],second_prob