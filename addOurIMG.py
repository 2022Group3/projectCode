import cv2
from matplotlib import image as mpimg, pyplot as plt
import os
import params


def save_our_img():
    ourImages=os.path.join(params.base_dir,params.our_img_folderName)
    for imgName in os.listdir(ourImages):
        print("imgName: "+imgName)
        imgPath=os.path.join(ourImages,imgName)
        print("imgPath: "+imgPath)
        img = cv2.imread(imgPath)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # this converts it into RGB
        plt.imshow(rgb_img)
        plt.show()
        label=input("Enter class label: ")
        img=cv2.resize(img, (32,32), interpolation = cv2.INTER_LANCZOS4)
        path_to_img=os.path.join(params.base_dir,params.extract_img_folderName,label,imgName)
        cv2.imwrite(path_to_img, img)

if __name__ == '__main__':
    save_our_img()
