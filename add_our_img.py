from matplotlib import image as mpimg, pyplot as plt
import os
import cv2
import pandas as pd
import params
import create_data_csv
import  pandas
import create_data_csv
from typing import Dict
import numpy as np
from skimage import io


def save_the_img(path,img):
    cv2.imwrite(path, img)


# change the img to 32X32 format
def change_img_size(img):
    resized = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LANCZOS4)
    return resized


def add_imgs_to_csv(dict1):
    print(dict1)
    df = pd.DataFrame(dict1)
    unique_df = create_data_csv.load_csv().drop_duplicates(params.csv_cols[4])

    # def a(row):
    #     lname = row['label_name']
    #     unique_row = unique_df[unique_df['label_name'] == lname]
    #     return unique_row[params.csv_cols[2]]
    #
    #
    # df[params.csv_cols[2]] = df.apply(a, axis=1)

    df[params.csv_cols[2]] = df['label_name'].apply(lambda row: ((unique_df[unique_df['label_name'] == row])[params.csv_cols[2]]))
    df[params.csv_cols[3]] = df['label_name'].apply(lambda row: ((unique_df[unique_df['label_name'] == row])[params.csv_cols[3]]))

    # labelscifar10 = create_data_csv.label_cifar10()
    # labelscifar100 = create_data_csv.label_cifar100()
    # labelscifar100chosen = [labelscifar100[x-1] for x in params.chosen_label]
    #
    # df[params.csv_cols[2]] = df['label_name'].apply(lambda label_name: )
    #
    # # df[params.csv_cols[2]] = df['label_name'].apply(lambda label_name: ([*range(1, len(labelscifar10)+1)]+params.chosen_label)[(label_cifar.index(bytes(label_name, 'utf-8')))] if bytes(label_name,'utf-8') in label_cifar else -1)
    #
    # df['current_label_number'] = df['label_name'].apply(lambda label_name: label_cifar.index(bytes(label_name, 'utf-8'))+1 if bytes(label_name, 'utf-8') in label_cifar else -1)
    create_data_csv.data_to_csv(df)


def save_our_img():
    # df=pd.DataFrame(columns=params.csv_cols)
    our_images = os.path.join(params.base_dir, params.our_img_folderName)
    images = os.listdir(our_images)
    dict1 = {}
    for col in params.csv_cols:
        dict1[col] = [None]*len(images)
    for i in range(len(images)):

        print("imgName: "+images[i])
        img_path = os.path.join(our_images, images[i])
        print("imgPath: "+img_path)
        img = cv2.imread(img_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # this converts it into RGB
        plt.imshow(rgb_img)
        plt.axis('off')
        plt.show()
        label = input("Enter class label: ")
        img = change_img_size(img)
        path_to_img = os.path.join(params.base_dir, params.extract_img_folderName, label, images[i])

# add info to dict
        dict1[params.csv_cols[0]][i] = images[i]
        dict1[params.csv_cols[1]][i] = "our_batch"
        dict1[params.csv_cols[4]][i] = label
        dict1[params.csv_cols[5]][i] = "our_dataset"
        dict1[params.csv_cols[6]][i] = "test"



        save_the_img(path_to_img, img)
    add_imgs_to_csv(dict1)
