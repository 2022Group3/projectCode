import pandas as pd
from os.path import exists
import os
import params
from DATA import extract_images_from_pickle as extract
import pickle
import logging
cols = params.csv_cols
base_dir = params.base_dir
labels=extract.get_labels_name()

# write to csv
def data_to_csv(data_frame:pd.DataFrame,path=params.csv_path,cols=params.csv_cols) -> None:
    logging.info("data_to_csv")
    if exists(path):
        data_frame.to_csv(path, mode='a', index=False, header=False)
    else:
        data_frame.to_csv(path, mode='a', index=False, header=cols)


# create dataFrame from cfar100
def cifar100_to_df() -> None:
    logging.info("cifar100_to_df")
    train = extract.unpickle(os.path.join(params.base_dir, "cifar-100-python", "train"))
    test = extract.unpickle(os.path.join(params.base_dir, "cifar-100-python", "test"))
    names = extract.label_cifar100()
    train_current_labels = [params.chosen_label.index(x)+10 if x in params.chosen_label else -1 for x in train[b'coarse_labels']]
    test_current_labels = [params.chosen_label.index(x)+10 if x in params.chosen_label else -1 for x in test[b'coarse_labels']]
    chosen_label = params.chosen_label
    # train dataFrame
    list_file_names = [x.decode('utf-8') for x in train[b'filenames'] ]
    df_train = pd.DataFrame({cols[0]: list_file_names, cols[1]: 'train', cols[2]: train[b'coarse_labels'],
                             cols[3]: train_current_labels, cols[4]: "", cols[5]: 'cifar100', cols[6]: ''})
    # test dataFrame
    list_file_names = [x.decode('utf-8') for x in test[b'filenames']]
    df_test = pd.DataFrame({cols[0]: list_file_names, cols[1]: 'test', cols[2]: test[b'coarse_labels'],
                            cols[3]: test_current_labels, cols[4]: "", cols[5]: 'cifar100', cols[6]: ''})
    # filter class, append train+test
    chosen_label_df = df_train[df_train[cols[2]].isin(chosen_label)].append(df_test[df_test[cols[2]].isin(chosen_label)])
    chosen_label_df['label_name'] = chosen_label_df.apply(lambda row: (names[row.original_label_number]).decode("utf-8"), axis=1)
    data_to_csv(chosen_label_df)


# create dataFrame from batch
def batch_df(dict:dict, batch_label:str, names:list[str]) -> pd.DataFrame:
    logging.info("batch_df")
    # create dataframe
    list_file_names = [x.decode('utf-8') for x in dict[b'filenames']]
    df = pd.DataFrame({cols[0]: list_file_names, cols[1]: batch_label,
                       cols[2]: dict[b'labels'], cols[3]: dict[b'labels'],
                       cols[4]: "", cols[5]: 'cifar10', cols[6]: ""})
    df['label_name'] = df.apply(lambda row: (names[row.original_label_number]).decode("utf-8"), axis=1)
    return df


# create dataFrame from cifar10
def cifar10_to_df() -> None:
    logging.info("cifar10_to_df")
    names = extract.label_cifar10()
    batch_files = [fn for fn in os.listdir(f'{base_dir}\\cifar-10-batches-py')
                   if (fn.startswith("data") or fn.startswith("test"))]
    for i in batch_files:
        dict = extract.unpickle(f'{base_dir}\\cifar-10-batches-py\\{i}')
        df = batch_df(dict, i, names)
        data_to_csv(df)


def load_csv(path=params.csv_path) -> pd.DataFrame:
    """
    load CSV file to dataframe
    :param path: CSV path
    :return: dataframe with CSV data
    """
    logging.info("load_csv: "+path)
    return pd.read_csv(path)


def extract_cifar() -> None:
    logging.info("extract_cifar")
    cifar10_to_df()
    cifar100_to_df()