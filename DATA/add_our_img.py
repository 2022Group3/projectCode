import cv2
import pandas as pd
from matplotlib import pyplot as plt
import os
import params
from DATA import create_data_csv
from DATA import extract_images_from_pickle as extract

labelscifar10 = extract.label_cifar10()
labelscifar10 = [x.decode('utf-8') for x in labelscifar10]
labelscifar100 = extract.label_cifar100()
labelscifar100 = [x.decode('utf-8') for x in labelscifar100]

def save_the_img(path, img):
    cv2.imwrite(path[:-3]+"png", img)


# change the img to 32X32 format
def change_img_size(img):
    resized = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LANCZOS4)
    return resized

def save_single_image(label,img_base_path,image_name):
    print("save_single_image")
    img = change_img_size(cv2.imread(img_base_path))
    path_to_img = os.path.join(params.base_dir, params.extract_img_folderName, label, image_name[:-3]+"png")
    df = pd.DataFrame(columns=params.csv_cols)
    save_the_img(path_to_img, img)
    df[params.csv_cols[0]] = [image_name[:-3]+"png"]
    df[params.csv_cols[1]] = ["our_batch"]
    df[params.csv_cols[4]] = [label]
    df[params.csv_cols[5]] = ["our_dataset"]
    df[params.csv_cols[6]] = ["test"]
    if label in labelscifar10:
        df[params.csv_cols[2]]=[labelscifar10.index(label)]
        df[params.csv_cols[3]]=[labelscifar10.index(label)]
    else:
        df[params.csv_cols[2]]=[labelscifar100.index(label)]
        df[params.csv_cols[3]]=[labelscifar100.index(label)+10]
    create_data_csv.data_to_csv(df)

# def save_our_img():
#     ourImages = os.path.join(params.base_dir, params.our_img_folderName)
#     images = os.listdir(ourImages)
#     df = pd.DataFrame(columns=params.csv_cols)
#     df[params.csv_cols[0]] = images
#     for i in range(len(images)):
#         print("imgName: "+images[i])
#         imgPath = os.path.join(ourImages, images[i])
#         print("imgPath: "+imgPath)
#         img = cv2.imread(imgPath)
#         rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # this converts it into RGB
#         plt.imshow(rgb_img)
#         plt.axis('off')
#         plt.show()
#         label = input("Enter class label: ")
#         img = change_img_size(img)
#         path_to_img = os.path.join(params.base_dir, params.extract_img_folderName, label, images[i])
#         save_the_img(path_to_img, img)
#         df.loc[i][params.csv_cols[0]] = images[i][:-3]+"png"
#         df.loc[i][params.csv_cols[1]] = "our_batch"
#         df.loc[i][params.csv_cols[4]] = label
#         df.loc[i][params.csv_cols[5]] = "our_dataset"
#         df.loc[i][params.csv_cols[6]] = "test"
#
#
#     df[params.csv_cols[2]] = df['label_name'].apply(
#         lambda label_name: labelscifar10.index(label_name) if label_name in labelscifar10 else labelscifar100.index(
#             label_name))
#     df[params.csv_cols[3]] = df['label_name'].apply(
#         lambda label_name: labelscifar10.index(label_name) if label_name in labelscifar10 else labelscifar100.index(
#             label_name) + 10)
#     create_data_csv.data_to_csv(df)
# if __name__ == '__main__':
#     save_single_image("flowers", r"D:\bootcamp\AMAT\project\cam.png", "cat.png")

