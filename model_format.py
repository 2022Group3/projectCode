# load train and test dataset
import params
import create_data_csv
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


def load_dataset():
    # load csv
    df = create_data_csv.load_csv()
    train_df = df[df[params.csv_cols[6]] == 'train']
    validation_df = df[df[params.csv_cols[6]] == 'validation']
    test_df = df[df[params.csv_cols[6]] == 'test']

    trainX, trainy = imgs_and_labels_from_df(train_df)
    validationX, validationy = imgs_and_labels_from_df(validation_df)
    testX, testy = imgs_and_labels_from_df(test_df)

    # # one hot encode target values
    # trainY = to_categorical(trainY)
    # testY = to_categorical(testY)
    np.savez('data_modified.npz', train=trainX, ytrain=trainy, validation=validationX, yvalidation=validationy,
             test=testX, ytest=testy)
    return trainX, trainy, validationX, validationy, testX, testy


if __name__ == '__main__':
    load_dataset()
