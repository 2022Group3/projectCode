
import params
import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#func that add to figure img by specific class
def createPlotOnFigByClass(numIMG,className,fig,indexFig,heightFig):
    pathToLabel=os.path.join(params.base_dir,"datasetImages",className)
    images=os.listdir(pathToLabel)
    images=sample(images,numIMG)
    for i in range(len(images)):
        pathToIMG = os.path.join(pathToLabel,images[i])
        ax = fig.add_subplot(heightFig,numIMG, indexFig+i)
        img = mpimg.imread(pathToIMG)
        plt.imshow(img)
        plt.axis('off')
        #ax.set_title(className,fontsize=5)

def displayIMGbyClass(numIMG,className):
    fig = plt.figure(figsize=(10, 10))
    createPlotOnFigByClass(numIMG, className, fig, 1,1)
    plt.show()

def displaySampleFromDataset(numIMG):
    indexFig=1
    fig = plt.figure(figsize=(10, 10))
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
