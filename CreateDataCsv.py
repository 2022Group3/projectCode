import pandas as pd
from os.path import exists
import os
import params

cols = params.csv_cols
base_dir = params.base_dir

# unpickle
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


# write to csv
def data_to_csv(dataFrame):
    if exists(params.CSV_path):
        dataFrame.to_csv(params.CSV_path, mode='a', index=False, header=False)
    else:
        dataFrame.to_csv(params.CSV_path, mode='a', index=False, header=cols)

def label_cifar100():
    return unpickle(os.path.join(params.base_dir,"cifar-100-python","meta"))[b'coarse_label_names']

# create dataFrame from cfar100
def cfar100_to_df():
    train = unpickle(os.path.join(params.base_dir,"cifar-100-python","train"))
    test = unpickle(os.path.join(params.base_dir,"cifar-100-python","test"))
    names =label_cifar100()
    train_current_labels = [x+10 for x in train[b'coarse_labels']]
    test_current_labels = [x+10 for x in test[b'coarse_labels']]
    chosen_label = params.chosen_label
    # train dataFrame
    df_train = pd.DataFrame({cols[0]: train[b'filenames'], cols[1]: 'train', cols[2]: train[b'coarse_labels'],
                             cols[3]: train_current_labels, cols[4]: "", cols[5]: 'cfar100', cols[6]: ''})
    # test dataFrame
    df_test = pd.DataFrame({cols[0]: test[b'filenames'], cols[1]: 'test', cols[2]: test[b'coarse_labels'],
                            cols[3]: test_current_labels, cols[4]: "", cols[5]: 'cfar100', cols[6]: ''})
    # filter class, append train+test
    chosen_label_df = df_train[df_train[cols[2]].isin(chosen_label)].append(df_test[df_test[cols[2]].isin(chosen_label)])
    print("1")
    chosen_label_df['label_name'] = chosen_label_df.apply(lambda row: (names[row.original_label_number]).decode("utf-8"), axis=1)
    print("1")
    print(chosen_label_df)
    data_to_csv(chosen_label_df)



# create dataFrame from batch
def batch_df(dict, batch_label, names):
    # create dataframe
    df = pd.DataFrame({cols[0]: dict[b'filenames'], cols[1]: batch_label,
                       cols[2]: dict[b'labels'], cols[3]: dict[b'labels'], cols[4]: "", cols[5]: 'cifar10', cols[6]: ""})
    df['label_name'] = df.apply(lambda row: (names[row.original_label_number]).decode("utf-8"), axis=1)
    return df

def label_cifar10():
    return unpickle(f'{base_dir}\\cifar-10-batches-py\\batches.meta')[b'label_names']
# create dataFrame from cifar10
def cfar10_to_df():
    names = label_cifar10()
    batch_files = [fn for fn in os.listdir(f'{base_dir}\\cifar-10-batches-py')
                   if (fn.startswith("data") or fn.startswith("test"))]
    for i in batch_files:
        dict = unpickle(f'{base_dir}\\cifar-10-batches-py\\{i}')
        df = batch_df(dict, i, names)
        data_to_csv(df)


# def ourPicturesDf(path):
#     dict = unpickle(path)
#     df = pd.DataFrame({'image_name': dict[b'filenames'],
#                        'batch_label': "", 'label_number':dict[b'label_num'], 'label_name': dict[b'label_name'], 'dataset': 'our',
#                        'train/validation/test': "test"})
#     data_to_csv(df)
#

if __name__ == '__main__':
     cfar10_to_df()
     cfar100_to_df()