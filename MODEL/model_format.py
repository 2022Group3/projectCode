# load train and test dataset
import params
from DATA import create_data_csv, extract_images_from_pickle
import os
import cv2
import numpy as np


def imgs_and_labels_from_df(df, count=None):
    labels = []
    images = []
    for index, row in df.iterrows():
        img_path = os.path.join(params.base_dir, params.extract_img_folderName, row[params.csv_cols[4]], row[params.csv_cols[0]])
        print(img_path)
        img = cv2.imread(img_path)
        images.append(img)
        labels.append(row[params.csv_cols[3]])
    return (images, labels)


def write_data_to_npz_file():
    # load csv
    df = create_data_csv.load_csv()
    train_df = df[df[params.csv_cols[6]] == 'train']

    validation_df = df[df[params.csv_cols[6]] == 'validation']
    test_df = df[df[params.csv_cols[6]] == 'test']
    our_test_df = test_df[test_df[params.csv_cols[5]] == 'our_dataset']
    cifar_test_df = test_df[test_df[params.csv_cols[5]] != 'our_dataset']

    # trainX, trainy = imgs_and_labels_from_df(train_df)
    # validationX, validationy = imgs_and_labels_from_df(validation_df)
    # testX, testy = imgs_and_labels_from_df(test_df)
    our_testX,our_testy=imgs_and_labels_from_df(our_test_df)

    np.savez('data_modified.npz',
                our_test=our_testX, our_ytest=our_testy)
#return trainX, trainy, validationX, validationy, cifar_testX, cifar_testy, our_testX, our_testy

def write_our_image_to_npz(csv_path):
    labels=extract_images_from_pickle.get_labels_name()
    df=create_data_csv.load_csv(csv_path)
    testY=[]
    testX=[]
    for index, row in df.iterrows():
        testY.append(labels.index(row['label']))
        img_path=os.path.join(params.base_dir,params.our_img_folderName,row['img_name'])
        print(img_path)
        img=cv2.imread(img_path)
        testX.append(img)
    np.savez('our_image_analyze.npz',test=testX, ytest=testY)





if __name__ == '__main__':
    #write_data_to_npz_file()
    write_our_image_to_npz(r"D:\bootcamp\AMAT\project\img_analyze.csv")