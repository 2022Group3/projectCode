# load train and test dataset
import params
from DATA import create_data_csv
import os
import cv2
import numpy as np


def imgs_and_labels_from_df(df):
    labels = []
    images = []
    for index, row in df.iterrows():
        img_path = os.path.join(params.base_dir, params.extract_img_folderName, row[params.csv_cols[4]], row[params.csv_cols[0]])
        print(img_path)
        img = cv2.imread(img_path)
        images.append(img)
        labels.append(row[params.csv_cols[3]])
    return images, labels


def write_data_to_npz_file():
    # load csv
    df = create_data_csv.load_csv()
    train_df = df[df[params.csv_cols[6]] == 'train']
    validation_df = df[df[params.csv_cols[6]] == 'validation']
    test_df = df[df[params.csv_cols[6]] == 'test']
    our_test_df = test_df[test_df[params.csv_cols[5]] == 'our_dataset']
    cifar_test_df = test_df[test_df[params.csv_cols[5]] != 'our_dataset']


    trainX, trainy = imgs_and_labels_from_df(train_df)
    validationX, validationy = imgs_and_labels_from_df(validation_df)
    testX, testy = imgs_and_labels_from_df(test_df)
    cifar_testX, cifar_testy = imgs_and_labels_from_df(cifar_test_df)
    our_testX, our_testy = imgs_and_labels_from_df(our_test_df)


    # # one hot encode target values
    # trainY = to_categorical(trainY)
    # testY = to_categorical(testY)
    np.savez('data_modified.npz', train=trainX, ytrain=trainy, validation=validationX, yvalidation=validationy,
             test=testX, ytest=testy)#,
             #cifar_test=cifar_testX, cifar_ytest=cifar_testy, our_test=our_testX, our_ytest=our_testy)
    #return trainX, trainy, validationX, validationy, cifar_testX, cifar_testy, our_testX, our_testy


if __name__ == '__main__':
    write_data_to_npz_file()

