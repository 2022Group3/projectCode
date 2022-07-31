from __future__ import print_function
import numpy as np
import pickle
import cv2
import os
import params
import logging


def unpickle(file: os.path) -> dict:
    """
    extract pickle file to dict
    :param file:
    :return: dict of the extract pickle
    """
    logging.info("unpickle")
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


def get_labels_name() -> list[str]:
    """
    concatenate all the labels name to one list
    :return: list of all the labels name
    """
    logging.info("get_labels_name")
    labelscifar10 = label_cifar10()
    labelscifar10 = [x.decode('utf-8') for x in labelscifar10]
    labelscifar100 = label_cifar100()
    labelscifar100 = [x.decode('utf-8') for x in labelscifar100]
    labelscifar100_chosen = [labelscifar100[x] for x in params.chosen_label]
    labels = labelscifar10 + labelscifar100_chosen
    return labels


def load_cifar10_pickle(path: os.path, file:os.path)-> tuple:
    """
    load specific pickle from cifar10
    :param path: path to the cifar10 folder
    :param file: the pickle-file name
    :return: list of the extract images, list of the extract lables, list of the image's name
    """
    logging.info(load_cifar10_pickle)
    dict = unpickle(os.path.join(path, file))
    images = dict[b'data']
    images = np.reshape(images, (len(images), 3, 32, 32))
    labels = np.array(dict[b'labels'])
    image_name = np.array(dict[b'filenames'])
    return images, labels, image_name


def save_cifar_image(array: np.array, path: os.path) -> cv2:
    """
    save specific image
    :param array: the image pixels array
    :param path: path to  the image save
    :return: the image after saving
    """
    logging.info("save_cifar_image")
    array = array.transpose(1, 2, 0)
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    return cv2.imwrite(path, array)


def extract_cifar10_batch(batch: str, categories: list) -> None:
    """

    :param batch: the name of the batch
    :param categories: list of all the labels in cifar10
    :return: None
    """
    logging.info("extract_cifar10_batch")
    images, labels, image_name = load_cifar10_pickle(os.path.join(params.base_dir, 'cifar-10-batches-py'), batch)
    for i in range(0, len(labels)):
        cat = categories[labels[i]]
        cat = cat.decode('utf-8')
        out_dir = os.path.join(params.base_dir, 'datasetImages', cat)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        save_cifar_image(images[i], os.path.join(out_dir, image_name[i].decode('utf-8')))


def load_cifar100_pickle(path: os.path, file: str) -> tuple:
    """
    load specific pickle from cifar100
    :param path: path to the cifar100 folder
    :param file: the pickle-file name
    :return: list of the extract images, list of the extract lables, list of the image's name
    """
    logging.info("load_cifar100_pickle")
    dict = unpickle(os.path.join(path, file))
    images = dict[b'data']
    labels = dict[b'coarse_labels']
    images = np.reshape(images, (len(images), 3, 32, 32))
    image_name = np.array(dict[b'filenames'])
    return images, labels, image_name


def label_cifar100() -> list:
    """
    extract the cifar100 labels
    :return: list of the cifar100 labels
    """
    logging.info("label_cifar100")
    return unpickle(os.path.join(params.base_dir, "cifar-100-python", "meta"))[b'coarse_label_names']


def label_cifar10() ->list:
    """
    extract the cifar10 labels
    :return: list of the cifar10 labels
    """
    logging.info("label_cifar10")
    return unpickle(f'{params.base_dir}\\cifar-10-batches-py\\batches.meta')[b'label_names']


def extract_cifar100_batch(batch, categories):
    logging.info("extract_cifar100_batch")
    images, labels, image_name = load_cifar100_pickle(os.path.join(params.base_dir, 'cifar-100-python'), batch)
    for i in range(0, len(labels)):
        if labels[i] in params.chosen_label:
            cat = categories[labels[i]]
            cat = cat.decode('utf-8')
            out_dir = os.path.join(params.base_dir, 'datasetImages', cat)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            save_cifar_image(images[i], f"{out_dir}\\{image_name[i].decode('utf-8')}")


def extract_cifar_data() -> None:
    """
    extract cifar10 and cifar100
    :return: None
    """
    logging.info("extract_cifar_data")
    categories10 = label_cifar10()
    categories100 = label_cifar100()
    extract_cifar100_batch('test', categories100)
    extract_cifar100_batch('train', categories100)

    for i in range(1, 6):
        extract_cifar10_batch(f'data_batch_{i}', categories10)

    extract_cifar10_batch('test_batch', categories10)