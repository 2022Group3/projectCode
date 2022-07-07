import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import params

#display specific image
# def display_image(image_name):
#     # creating a object
#     path=os.path.join((params.base_dir,'datasetImages'),)
#     im = Image.open(params.base_dir.)
#     im.show()


#func that add to figure img by specific class
def createPlotOnFigByClass(numIMG,className,fig,indexFig,heightFig):
    pathToLabel=os.path.join(params.base_dir,"datasetImages",className)
    images=os.listdir(pathToLabel)
    images=sample(images,numIMG)
    ax = fig.add_subplot(heightFig, numIMG, indexFig)
    plt.axis('off')
    ax.text(0,0,className, style='italic',
            fontsize=10, color="black")
    for i in range(1,len(images)):
        pathToIMG = os.path.join(pathToLabel,images[i-1])
        ax = fig.add_subplot(heightFig,numIMG, indexFig+i)
        img = mpimg.imread(pathToIMG)
        plt.imshow(img)
        plt.axis('off')
        #ax.set_title(className,fontsize=5)

def displayIMGbyClass(numIMG,className):
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle("display "+className)
    createPlotOnFigByClass(numIMG+1, className, fig, 1,1)
    plt.show()

def displaySampleFromDataset(numIMG):
    indexFig=1
    numIMG+=1
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle('display sample')
    datasetImages=os.path.join(params.base_dir,"datasetImages")
    for label in os.listdir(datasetImages):
        createPlotOnFigByClass(numIMG, label, fig, indexFig, 10+len(params.chosen_label))
        indexFig+=numIMG
    plt.show()



if __name__ == '__main__':
    #displaySampleFromDataset(base_dir, 8)
    displayIMGbyClass(3, "dog")
    #displayIMGbyClass(5, "dog")
    displaySampleFromDataset(15)
