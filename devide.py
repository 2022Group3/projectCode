#devide to train ,validation and test
import pandas as pd
import numpy as np

def train_validate_test_split(csv_data, train_percent=0.6, validate_percent=0.1, seed=None):
    df = pd.read_csv(csv_data)
    df.drop('train/validation/test', inplace=True, axis=1)
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    validate_end = int(validate_percent * m) + train_end
    train = df.iloc[perm[:train_end]]
    validate = df.iloc[perm[train_end:validate_end]]
    test = df.iloc[perm[validate_end:]]
    train['train/validation/test']='train'
    validate['train/validation/test']='validation'
    test['train/validation/test']='test'
    dataframe=train.append(validate).append(test)
    dataframe.to_csv('df.csv')
    return dataframe

# def train_validate_test_split(csv_data, train_percent=0.6, validate_percent=0.1):
#     df = pd.read_csv(csv_data)
#     df.drop('train/validation/test', inplace=True, axis=1)

if __name__ == '__main__':
    file=r"C:\D\bootcamp\project\projectCode\data.csv"
    print(train_validate_test_split(file))