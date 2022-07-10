import os
import cv2
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import params
import CreateDataCsv
import pandas as pd

#display specific image
# def display_image_by_name(image_name):
#     df=CreateDataCsv.load_csv()
#     df=((df[df['image_name']==image_name]))
#     df.reset_index()
#     image_label=df.iloc[0]['label_name']
#     image_path=os.path.join(params.base_dir,'datasetImages',image_label,image_name)
#     img = cv2.imread(image_path)
#     plt.imshow(img)
#     plt.axis('off')
#     plt.show()



#func that add to figure img by specific class
def createPlotOnFigByClass(numIMG,className,fig,indexFig,heightFig,from_all=False):
    pathToLabel=os.path.join(params.base_dir,"datasetImages",className)
    images=os.listdir(pathToLabel)
    images=sample(images,numIMG)
    s = 0
    if from_all==True:
        ax = fig.add_subplot(heightFig, numIMG, indexFig)
        plt.axis('off')
        ax.text(0,0,className, style='italic',
                fontsize=5,color="black")
        s=1
    for i in range(s,len(images)):
        pathToIMG = os.path.join(pathToLabel,images[i-s])
        ax = fig.add_subplot(heightFig,numIMG, indexFig+i)
        img = mpimg.imread(pathToIMG)
        plt.imshow(img)
        plt.axis('off')
        #ax.set_title(className,fontsize=5)

def displayIMGbyClass(numIMG,className):
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle("display "+className)
    createPlotOnFigByClass(numIMG, className, fig, 1,1)
    plt.show()

def displaySampleFromDataset(numIMG):
    indexFig=1
    numIMG+=1
    fig = plt.figure(figsize=(10,10))
    fig.suptitle('display sample')
    datasetImages=os.path.join(params.base_dir,"datasetImages")
    for label in os.listdir(datasetImages):
        createPlotOnFigByClass(numIMG, label, fig, indexFig, 10+len(params.chosen_label),True)
        indexFig+=numIMG
    plt.show()



if __name__ == '__main__':
    # display_image_by_name('bottle_s_001976.png')
    #displaySampleFromDataset(base_dir, 8)
    #displayIMGbyClass(3, "cat")
    displayIMGbyClass(5, "dog")
    displaySampleFromDataset(15)
