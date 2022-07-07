
import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import params

import os
from random import sample
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
# import os
# from random import sample
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import cv2
# import seaborn as sns
# import params
# from PIL import Image
#
# def displayIMGbyClass(base_dir,numIMG,className):
#     fig = plt.figure(figsize=(32,32))
#     pathToLabel=os.path.join(base_dir,"datasetImages")
#     pathToLabel=os.path.join(pathToLabel,className)
#     images=os.listdir(pathToLabel)
#     images=sample(images,numIMG)
#     for i in range(len(images)):
#         pathToIMG = os.path.join(pathToLabel,images[i])
#         ax = fig.add_subplot(1,numIMG, i+1)
#         img = mpimg.imread(pathToIMG)
#         imgplot = plt.imshow(img)
#         ax.set_title(images[i])
#     plt.show()
#
#
# def func2(base_dir,numIMG):
#     rows=15
#     columns=numIMG
#     fig = plt.figure(figsize=(32, 32))
#     image_file = os.path.join(base_dir,"datasetImages")
#     a=[]
#     for label in os.listdir(image_file):
#         label_path=os.path.join(image_file,label)
#         for image in os.listdir(label_path):
#             image_path=os.path.join(label_path,image)
#             a.append(Image.open(image_path))
#         os.close(label_path)
#     os.close(image_file)
#     for i in range(1,rows*columns+1):
#         fig.add_subplot(rows,columns, i)
#         plt.imshow(a[i])
#     plt.show()
#
#
#
#
#
# # def func(base_dir,numIMG,className):
# #     fig, axes = plt.subplots(15, numIMG, figsize=(32,32), sharex=True, sharey=True)
# #     for i, ax in enumerate(axes.flat):
# #         im = ax.imshow(np.exp(W_[:, :, i]), cmap='RdBu', vmin=0.7, vmax=1.3)
# #         ax.set_title(i)
# #     ax.set(xticks=[], yticks=[])
# #     fig.tight_layout()
# #     sns.despine(bottom=True, left=True)
# # def func(base_dir,numIMG):
#
# def func1(base_dir,numIMG,labels):
#     lab=0
#     rows=15
#     columns=numIMG
#     pathToLabel = os.path.join(base_dir, "datasetImages")
#     fig = plt.figure(figsize=(32,32))
#     for i in range(rows*columns):
#         fig.add_subplot(rows, columns, lab+1)
#         pathToLabel=os.path.join(pathToLabel,labels[lab])
#         images = os.listdir(pathToLabel)
#         images = sample(images, numIMG)
#         for j in images:
#             type(j)
#             img = cv2.imread(j)
#             type(img)
#             plt.imshow(img)
#             plt.axis('off')
#         pathToLabel = os.path.join(base_dir, "datasetImages")
# def displaySampleFromDataset(base_dir,numIMG):
#     datasetImages=os.path.join(base_dir,"datasetImages")
#     for labelIMG in os.listdir(datasetImages):
#         displayIMGbyClass(base_dir,numIMG,labelIMG)
#

if __name__ == '__main__':
    base_dir = r"C:\D\bootcamp\project\dataset"
    #displaySampleFromDataset(base_dir, 8)
    print("CDF")
    #displayIMGbyClass(15, "dog")
    #displayIMGbyClass(5, "dog")
    print("vv")
    displaySampleFromDataset(6)

