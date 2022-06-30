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
def data_to_csv(data):
    data.to_csv('data.csv',mode='a',index=False,header=False)


# create dataFrame from cfar100
def cfar100ToDf(picklePath, chosen_label=2):
    train = unpickle(picklePath + "\\train")
    test = unpickle(picklePath + "\\test")
    names=unpickle(picklePath+"\\meta")[b'coarse_label_names']

    def create_labelname(x):
        name = names[x]
        name = name.decode("utf-8")
        return name
    # train dataFrame
    df_train = pd.DataFrame({'image_name': train[b'filenames'], 'batch_label': train[b'batch_label'],
                             'label_number': train[b'coarse_labels'], 'dataset': 'cfar100',
                             'train/validation/test': 'train'})
    df_train['label_name']=df_train['label_number'].apply(create_labelname)

    # test dataFrame
    df_test = pd.DataFrame({'file_name': test[b'filenames'], 'batch_label': test[b'batch_label'],
                            'label_number': test[b'coarse_labels'], 'dataset': 'cfar100',
                            'train/validation/test': 'test'})
    df_test['label_name']=df_test['label_number'].apply(create_labelname)


    # filter class, append train+test
    chosen_label_df = df_train[df_train['label_number'] == chosen_label].append(
        df_test[df_test['label_number'] == chosen_label])
    chosen_label_df['id'] = np.arange(60001, 63001)

    # reorder columns
    cols=['id', 'image_name','batch_label', 'label_number', 'label_name', 'dataset','train/validation/test']
    chosen_label_df=chosen_label_df[cols]
    print(chosen_label_df)
    data_to_csv(chosen_label_df)

# create dataFrame from batch
def batch_df(dict,label_names,batch,batch_num):
    df = pd.DataFrame({'id':np.arange(batch_num*10000-9999,batch_num*10000+1),'image_name':dict[b'filenames'],
                       'batch_label':batch,'label_number':dict[ b'labels'],'dataset':'cifar10'})
    # label names
    label_names_array = []
    for i in df['label_number']:
        label_names_array.append(label_names[i])
    df['label_name'] = label_names_array
    # tain/validation/test
    if batch=='test_batch':
        type='test'
    else:
        type='train'
    data_type=np.full((len(dict[b'labels']),1),type)
    df['tain/validation/test']=data_type
    # reorder columns
    cols=['id','image_name','batch_label','label_number','label_name','dataset','tain/validation/test']
    chosen_label_df = df[cols]
    return df

# def batch_df(dict,label_names,batch,batch_num):
#     df=pd.DataFrame()
#     #id
#     indexes=np.arange(batch_num*10000-9999,batch_num*10000+1)
#     df['id']= indexes
#     #image name
#     df['image_name']=dict[b'filenames']
#     #bach label:
#     batch_array=np.full((len(dict[b'labels']),1),batch)
#     df['batch_label']=batch_array
#     # label num
#     df['label_number']=dict[ b'labels']
#     #label names
#     label_names_array=[]
#     for i in df['label_number']:
#         label_names_array.append(label_names[i])
#     df['label_name']=label_names_array
#     #dataset
#     dataset_array=np.full((len(dict[b'labels']),1),'cifar10')
#     df['dataset']=dataset_array
#     #tain/validation/test
#     if batch=='test_batch':
#         type='test'
#     else:
#         type='train'
#     data_type=np.full((len(dict[b'labels']),1),type)
#     df['tain/validation/test']=data_type
#     return df


# create dataFrame from cifar10
def cifar10Df(batch_file,label_names):
    for i in range(1,6):
        file=batch_file+'\data_batch_'+str(i)
        dict = unpickle(file)
        path_of_batch='data_batch_'+str(i)
        df = batch_df(dict, label_names, path_of_batch,i)
        data_to_csv(df)
    file = batch_file+'\\test_batch'
    dict = unpickle(file)
    path_of_batch='test_batch'
    df = batch_df(dict,label_names,path_of_batch, 6)
    data_to_csv(df)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
     batch_file=r"C:\D\bootcamp\project\dataset\cifar-10-batches-py"
     meta_file = r"C:\D\bootcamp\project\dataset\cifar-10-batches-py\batches.meta"
     meta_data = unpickle(meta_file)
     label_names = meta_data[b'label_names']
     cifar10Df(batch_file,label_names)
     cfar100ToDf(r"C:\D\bootcamp\project\dataset\cifar-100-python")
     #hello