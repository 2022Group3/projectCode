# load train and test dataset
import params
import create_data_csv
import os
import cv2

def func(row):
    img_path = os.path.join(params.base_dir, params.extract_img_folderName, row[params.csv_cols[0]])
    img = cv2.imread(img_path)
    lable = row[params.csv_cols[3]]


def load_dataset():
	# load csv
    df = create_data_csv.load_csv()
    train_df= df[df[params.csv_cols[6]] == 'train']
    validation_df= df[df[params.csv_cols[6]] == 'train']
    test_df = df[df[params.csv_cols[6]] == 'test']
    trainX, trainy = train_df.apply(func)
    validationX, validationy = validation_df.apply(func)
    testX, testy = test_df.apply(func)

    # # one hot encode target values
	# trainY = to_categorical(trainY)
	# testY = to_categorical(testY)
    print(trainX, trainy, validationX, validationy, testX, testy)
    return trainX, trainy, validationX, validationy, testX, testy

if __name__ == '__main__':
    load_dataset()