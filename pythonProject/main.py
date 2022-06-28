# This is a sample Python script.

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


data_batch_1=unpickle("C:\\Users\\Nechama\\Desktop\\bootcampProject\\cifar-10-python\\cifar-10-batches-py\\data_batch_1")

