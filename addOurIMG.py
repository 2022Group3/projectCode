import cv2
import pandas as pd
from matplotlib import image as mpimg, pyplot as plt
import os
import params
import CreateDataCsv
import  pandas
import CreateDataCsv
import numpy as np
from skimage import io



def saveTheIMG(path,img):
    cv2.imwrite(path, img)


#change the img to 32X32 format
def changeIMGSize(img):
    resized = cv2.resize(img, (32,32), interpolation = cv2.INTER_LANCZOS4)
    return resized

def addIMGStoTheCSV(dict1):
    df=pd.DataFrame(dict1)
    df['dataset']="our"
    df['train/validation/test'] = "test"
    labelscifar10=CreateDataCsv.label_cifar10()
    labelscifar100=CreateDataCsv.label_cifar100()
    labelscifar100chosen= [labelscifar100[x-1] for x in params.chosen_label]
    label_cifar=(labelscifar10 + labelscifar100chosen)
    df['current_label_number']=df['label_name'].apply(lambda label_name: label_cifar.index(bytes(label_name, 'utf-8'))+1 if bytes(label_name, 'utf-8') in label_cifar else -1)
    df['original_label_number']=df['label_name'].apply(lambda label_name: ([*range(1,len(labelscifar10)+1)]+params.chosen_label)[(label_cifar.index(bytes(label_name, 'utf-8')))] if bytes(label_name,'utf-8') in label_cifar else -1)
    CreateDataCsv.data_to_csv(df)

def save_our_img():
    #df=pd.DataFrame(columns=params.csv_cols)
    ourImages=os.path.join(params.base_dir,params.our_img_folderName)
    images=os.listdir(ourImages)
    dict1={}
    for col in params.csv_cols:
        dict1[col]=[None]*len(images)
    for i in range(len(images)):
        print("imgName: "+images[i])
        imgPath=os.path.join(ourImages,images[i])
        print("imgPath: "+imgPath)
        #img = cv2.imread(imgPath)
        #insted of the previos line' it's help me
        img = cv2.imread(imgPath)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # this converts it into RGB
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        label=input("Enter class label: ")
        img=changeIMGSize(img)
        path_to_img=os.path.join(params.base_dir,params.extract_img_folderName,label,'a'+images[i])

        dict1['image_name'][i]=images[i]
        dict1['label_name'][i]=label
        saveTheIMG(path_to_img,img)
    addIMGStoTheCSV(dict1)

if __name__ == '__main__':
    save_our_img()
