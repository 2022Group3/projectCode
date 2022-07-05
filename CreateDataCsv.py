# This is a sample Python script.
import pandas as pd
import numpy as np
# import ipython_genutils
# from Ipython.display import display


# unpickle
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict



# write to csv
def data_to_csv(data,cols=False):
    data.to_csv('data.csv',mode='a',index=False,header=cols)


# create dataFrame from cfar100
def cfar100ToDf(picklePath,chosen_label=[1,2,3,4,5]):
    train = unpickle(picklePath + "\\train")
    test = unpickle(picklePath + "\\test")
    names=unpickle(picklePath+"\\meta")[b'coarse_label_names']

    def create_labelname(x):
        name = names[x]
        name = name.decode("utf-8")
        return name
    # train dataFrame
    df_train = pd.DataFrame({'image_name': train[b'filenames'], 'batch_label': 'train',
                             'label_number': train[b'coarse_labels'],'label_name':"", 'dataset': 'cfar100',
                             'train/validation/test': 'train'})


    # test dataFrame
    df_test = pd.DataFrame({'image_name': test[b'filenames'], 'batch_label': 'test',
                            'label_number': test[b'coarse_labels'],'label_name':"",'dataset': 'cfar100',
                            'train/validation/test': 'test'})


    # filter class, append train+test
    chosen_label_df = df_train[df_train['label_number'].isin(chosen_label)].append(
        df_test[df_test['label_number'].isin(chosen_label)])
    chosen_label_df['label_name'] = chosen_label_df['label_number'].apply(create_labelname)

    print(chosen_label_df)
    data_to_csv(chosen_label_df)

# create dataFrame from batch
def batch_df(dict,label_names,batch,batch_num):
    # train/validation/test
    if batch=='test_batch':
        type='test'
    else:
        type='train'

    # label names
    def create_labelname(x):
        name = label_names[x]
        name = name.decode("utf-8")
        return name
    #create dataframe
    df = pd.DataFrame({'image_name':dict[b'filenames'],
                       'batch_label':batch,'label_number':dict[ b'labels'],'label_name':"",'dataset':'cifar10','train/validation/test':type})
    df['label_name']=df['label_number'].apply(create_labelname)
    return df


# create dataFrame from cifar10
def cifar10Df(batch_file,label_names,cols):
    for i in range(1,6):
        path_of_batch='data_batch_'+str(i)
        file=batch_file+'\\'+ path_of_batch
        dict = unpickle(file)
        df = batch_df(dict,label_names, path_of_batch,i)
        #within header
        if i==1:
            data_to_csv(df,cols)
        else:
            data_to_csv(df)
    path_of_batch='test_batch'
    file = batch_file+'\\'+path_of_batch
    dict = unpickle(file)
    df = batch_df(dict,label_names,path_of_batch, 6)
    data_to_csv(df)
# Press the green button in the gutter to run the script.



if __name__ == '__main__':
     batch_file=r"C:\D\bootcamp\project\dataset\cifar-10-batches-py"
     meta_file = r"C:\D\bootcamp\project\dataset\cifar-10-batches-py\batches.meta"
     meta_data = unpickle(meta_file)
     label_names = meta_data[b'label_names']
     cols = ['image_name','batch_label','label_number','label_name','dataset','train/validation/test']
     cifar10Df(batch_file,label_names,cols)
     cfar100_file=r"C:\D\bootcamp\project\dataset\cifar-100-python"
     cfar100ToDf(cfar100_file)

