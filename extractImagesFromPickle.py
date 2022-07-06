from __future__ import print_function
import numpy as np
import pickle
import cv2
import os

def load_cifar10_pickle(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    images = dict[b'data']
    images = np.reshape(images, (len(images), 3, 32, 32))
    labels = np.array(dict[b'labels'])
    image_name=np.array(dict[b'filenames'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels, image_name

def load_cifar10_categories(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    return dict[b'label_names']

def save_cifar_image(array, path):
    # array is 3x32x32. cv2 needs 32x32x3
    array = array.transpose(1,2,0)
    # array is RGB. cv2 needs BGR
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    # save to PNG file
    return cv2.imwrite(path,array)

def extract_cifar10_batch(base_dir,dataset,batch,categories):
    images, labels,image_name = load_cifar10_pickle(os.path.join(base_dir, dataset),batch)
    print(len(labels))
    for i in range(0,len(labels)):
        cat = categories[labels[i]]
        cat=cat.decode('utf-8')
        print(cat)
        out_dir = os.path.join(base_dir, 'datasetImages', cat)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        save_cifar_image(images[i], os.path.join(out_dir, image_name[i].decode('utf-8')))
#
def load_cifar100_pickle(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    images = dict[b'data']
    images = np.reshape(images, (len(images), 3, 32, 32))
    labels = np.array(dict[b'coarse_labels'])
    image_name=np.array(dict[b'filenames'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels, image_name

def load_cifar100_categories(path, file):
    f = open(os.path.join(path, file), 'rb')
    dict = pickle.load(f,encoding='bytes')
    return dict[b'coarse_label_names']

def extract_cifar100_batch(base_dir,dataset,batch,categories):
    images, labels,image_name = load_cifar100_pickle(os.path.join(base_dir, dataset),batch)
    for i in range(0,len(labels)):
        cat = categories[labels[i]]
        cat=cat.decode('utf-8')
        print(cat)
        out_dir = os.path.join(base_dir, 'datasetImages', cat)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        save_cifar_image(images[i], os.path.join(out_dir, image_name[i].decode('utf-8')))
if __name__ == '__main__':
    base_dir= r"D:\bootcamp\AMAT\project\dataset"
    #picke_name = 'data_batch_'
    categories10 = load_cifar10_categories(os.path.join(base_dir, 'cifar-10-batches-py'), "batches.meta")
    categories100=load_cifar100_categories(os.path.join(base_dir, 'cifar-100-python'), "meta")

    for i in range(1,6):
        extract_cifar10_batch(base_dir,'cifar-10-batches-py', 'data_batch_'+str(i),categories10)
    extract_cifar100_batch(base_dir, 'cifar-100-python', 'test',categories100)
    extract_cifar100_batch(base_dir, 'cifar-100-python', 'train',categories100)
