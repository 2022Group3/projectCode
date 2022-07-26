from __future__ import print_function
import numpy as np
import pickle
import cv2
import os
import params
# from DATA import create_data_csv


def unpickle(file):
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d
def get_labels_name():
    labelscifar10 = label_cifar10()
    labelscifar10 = [x.decode('utf-8') for x in labelscifar10]
    labelscifar100 = label_cifar100()
    labelscifar100 = [x.decode('utf-8') for x in labelscifar100]
    labelscifar100_chosen = [labelscifar100[x] for x in params.chosen_label]
    labels = labelscifar10 + labelscifar100_chosen
    return labels

def load_cifar10_pickle(path, file):
    dict = unpickle(os.path.join(path, file))
    images = dict[b'data']
    images = np.reshape(images, (len(images), 3, 32, 32))
    labels = np.array(dict[b'labels'])
    image_name = np.array(dict[b'filenames'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels, image_name


def save_cifar_image(array, path):
    # array is 3x32x32. cv2 needs 32x32x3
    array = array.transpose(1, 2, 0)
    # array is RGB. cv2 needs BGR
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    # save to PNG file
    return cv2.imwrite(path, array)


def extract_cifar10_batch(batch, categories):
    images, labels, image_name = load_cifar10_pickle(os.path.join(params.base_dir, 'cifar-10-batches-py'), batch)
    print(len(labels))
    for i in range(0, len(labels)):
        cat = categories[labels[i]]
        cat = cat.decode('utf-8')
        print(cat)
        out_dir = os.path.join(params.base_dir, 'datasetImages', cat)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        save_cifar_image(images[i], os.path.join(out_dir, image_name[i].decode('utf-8')))


def load_cifar100_pickle(path, file):
    dict = unpickle(os.path.join(path, file))
    images = dict[b'data']
    labels = dict[b'coarse_labels']
    images = np.reshape(images, (len(images), 3, 32, 32))
    image_name = np.array(dict[b'filenames'])
    print("Loaded {} labelled images.".format(images.shape[0]))
    return images, labels, image_name


def label_cifar100():
    return unpickle(os.path.join(params.base_dir, "cifar-100-python", "meta"))[b'coarse_label_names']


def label_cifar10():
    return unpickle(f'{params.base_dir}\\cifar-10-batches-py\\batches.meta')[b'label_names']


def extract_cifar100_batch(batch, categories):
    images, labels, image_name = load_cifar100_pickle(os.path.join(params.base_dir, 'cifar-100-python'), batch)
    for i in range(0, len(labels)):
        if labels[i] in params.chosen_label:
            cat = categories[labels[i]]
            print(cat)
            cat = cat.decode('utf-8')
            out_dir = os.path.join(params.base_dir, 'datasetImages', cat)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            save_cifar_image(images[i], f"{out_dir}\\{image_name[i].decode('utf-8')}")


def extract_cifar_data():
    categories10 = label_cifar10()
    categories100 = label_cifar100()
    extract_cifar100_batch('test', categories100)
    extract_cifar100_batch('train', categories100)

    for i in range(1, 6):
        extract_cifar10_batch(f'data_batch_{i}', categories10)

    extract_cifar10_batch('test_batch', categories10)
