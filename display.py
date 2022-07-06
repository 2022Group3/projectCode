import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def displayIMGbyClass(base_dir,numIMG,className):
    fig = plt.figure(figsize=(32,32))
    pathToLabel=os.path.join(base_dir,"datasetImages")
    pathToLabel=os.path.join(pathToLabel,className)
    images=os.listdir(pathToLabel)
    images=sample(images,numIMG)
    for i in range(len(images)):
        pathToIMG = os.path.join(pathToLabel,images[i])
        ax = fig.add_subplot(1,numIMG, i+1)
        img = mpimg.imread(pathToIMG)
        imgplot = plt.imshow(img)
        ax.set_title(images[i])


def displaySampleFromDataset(base_dir,numIMG):
    datasetImages=os.path.join(base_dir,"datasetImages")
    for labelIMG in os.listdir(datasetImages):
        displayIMGbyClass(base_dir,numIMG,labelIMG)



if __name__ == '__main__':
    base_dir=r"D:\bootcamp\AMAT\project\dataset"
    displaySampleFromDataset(base_dir, 8)

