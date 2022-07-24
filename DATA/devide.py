
import pandas as pd
import numpy as np
import params
from os.path import exists


def train_validate_test_split(csv_data=params.csv_path, train_percent=0.6, validate_percent=0.1, seed=None):
    # if exists(params.csv_path):
    #     df = pd.read_csv(csv_data)
    #     np.random.seed(seed)
    #     perm = np.random.permutation(df.index)
    #     df_len = len(df.index)
    #     train_end = int(train_percent * df_len)
    #     validate_end = int(validate_percent * df_len) + train_end
    #     train = df.iloc[perm[:train_end]]
    #     validate = df.iloc[perm[train_end:validate_end]]
    #     test = df.iloc[perm[validate_end:]]
    #     train[params.csv_cols[6]] = 'train'
    #     validate[params.csv_cols[6]] = 'validation'
    #     test[params.csv_cols[6]] = 'test'
    #     dataframe = train.append(validate).append(test)
    #     dataframe = dataframe.reset_index(drop=True)
    #     dataframe.to_csv(csv_data, index=False)
    #     return dataframe

    if exists(params.csv_path):
        df = pd.read_csv(csv_data)
        # np.random.seed(seed)
        df = df.sample(frac=1).reset_index(drop=True)
        df_len = len(df.index)
        train_end = int(train_percent * df_len)
        validate_end = int(validate_percent * df_len) + train_end
        df.loc[:train_end, params.csv_cols[6]] = 'train'
        df.loc[train_end:validate_end, params.csv_cols[6]] = 'validation'
        df.loc[validate_end:, params.csv_cols[6]] = 'test'
        df.to_csv(csv_data, index=False)
        return df


# if __name__ == '__main__':
#     print(train_validate_test_split())
