# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # data_batch_1=unpickle("C:\\D\\bootcamp\\project\\dataset\\cifar-10-batches-py\\data_batch_1")
    data_batch_1=unpickle(r"C:\D\bootcamp\project\dataset\cifar-100-python\test")
    meta= unpickle(r"C:\D\bootcamp\project\dataset\cifar-100-python\meta")
    print(data_batch_1.keys())

    # print(data_batch_1.keys())
    # print(data_batch_1[b'batch_label'])
    # print(type(data_batch_1))
    # X_train = data_batch_1[b'data']
    # image = data_batch_1[b'data'][0]
    # image = image.reshape(3, 32, 32)
    # image = image.transpose(1, 2, 0)
    # X_train = data_batch_1[b'data']
    # print("Shape before reshape:", image.shape)
    # X_train = X_train.reshape(len(X_train), 3, 32, 32)
    # print("Shape after reshape and before transpose:", image.shape)
    # # Transpose the whole data
    # X_train = X_train.transpose(0, 2, 3, 1)
    # print("Shape after reshape and transpose:", image.shape)
    # import matplotlib.pyplot as plt
    #
    # # label names
    # label_name = data_batch_1['label_names']
    # # take first image
    # image = data_batch_1['data'][0]
    # # take first image label index
    # label = data_batch_1['labels'][0]
    # # Reshape the image
    # image = image.reshape(3, 32, 32)
    # # Transpose the image
    # image = image.transpose(1, 2, 0)
    # # Display the image
    # plt.imshow(image)
    # plt.title(label_name[label])
    #
    # print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
