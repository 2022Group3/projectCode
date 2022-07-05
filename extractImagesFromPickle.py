from __future__ import print_function
import numpy as np
import pickle
import cv2
import os

def load_cifar_pickle(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    images = dict[b'data']
    images = np.reshape(images, (10000, 3, 32, 32))
    labels = np.array(dict[b'labels'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels


def load_cifar_categories(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    return dict[b'label_names']

def save_cifar_image(array, path):
    # array is 3x32x32. cv2 needs 32x32x3
    array = array.transpose(1,2,0)
    # array is RGB. cv2 needs BGR
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    # save to PNG file
    return cv2.imwrite(path, array)


if __name__ == '__main__':
    base_dir= r"C:\D\bootcamp\project\dataset"
    picke_name = 'data_batch_1'
    n_imgs = 10

    images, labels = load_cifar_pickle(os.path.join(base_dir, 'cifar-10-batches-py'), picke_name)
    categories = load_cifar_categories(os.path.join(base_dir, 'cifar-10-batches-py'), "batches.meta")
    print(categories)

    for i in range(0,n_imgs):
        cat = categories[labels[i]]
        cat=cat.decode('utf-8')
        print(cat)
        out_dir = os.path.join(base_dir, 'datasetImages', cat)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        save_cifar_image(images[i], os.path.join(out_dir, 'image_{}.png'.format(i)))