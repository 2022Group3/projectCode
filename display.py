#display!!!!!!!!!!!!!
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def display_image(array):

    rgbArray = np.zeros((32, 32, 3), 'uint8')
    rgbArray[..., 0] = array[:1024].reshape(32, 32)
    rgbArray[..., 1] = array[1024:2048].reshape(32, 32)
    rgbArray[..., 2] = array[2048:3072].reshape(32, 32)
    im = Image.fromarray(rgbArray)
    im.save("filename.jpeg")
    im.show()


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
       dict = pickle.load(fo, encoding='bytes')
    return dict



if __name__ == '__main__':
   batch_file=r"C:\D\bootcamp\project\dataset\cifar-10-batches-py\data_batch_1"
   dict=unpickle(batch_file)
   display_image(dict[b'data'][4])

   #im = Image.open(r"C:\Users\1\Downloads\86289.jpg")
   #im.show()