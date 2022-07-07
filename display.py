import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import params


base_dir = r"C:\D\bootcamp\project\dataset"
# ax.text(3, 4, 'GeeksforGeeks', style ='italic',
#         fontsize = 30, color ="green")
def createPlotOnFigByClass(numIMG,className,fig,indexFig,heightFig):
    pathToLabel=os.path.join(params.base_dir,"datasetImages",className)
    images=os.listdir(pathToLabel)
    images=sample(images,numIMG)
    ax = fig.add_subplot(heightFig,numIMG,indexFig)
    plt.axis('off')
    ax.text(0,0, className, style='italic',
           fontsize = 10,color ="black")
    for i in range(1,len(images)):
        pathToIMG = os.path.join(pathToLabel,images[i-1])
        ax = fig.add_subplot(heightFig,numIMG, indexFig+i)
        img = mpimg.imread(pathToIMG)
        plt.axis('off')
        imgplot = plt.imshow(img)
        # ax.set_title(images[i],fontsize=5)

def displayIMGbyClass(numIMG,className):
    fig = plt.figure(figsize=(10, 10))
    createPlotOnFigByClass(numIMG, className, fig, 1,1)
    plt.show()

def displaySampleFromDataset(numIMG):
    indexFig=1
    numIMG+=1
    fig = plt.figure(figsize=(20, 20))
    datasetImages=os.path.join(params.base_dir,"datasetImages")
    for label in os.listdir(datasetImages):
        createPlotOnFigByClass(numIMG, label, fig, indexFig, 10+len(params.chosen_label))
        indexFig+=numIMG
    plt.show()


if __name__ == '__main__':
    base_dir = r"C:\D\bootcamp\project\dataset"
    #displaySampleFromDataset(base_dir, 8)
    print("CDF")
    #displayIMGbyClass(15, "dog")
    #displayIMGbyClass(5, "dog")
    print("vv")
    displaySampleFromDataset(6)

