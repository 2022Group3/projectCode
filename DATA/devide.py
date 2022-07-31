
import pandas as pd
import numpy as np
import params
from os.path import exists
def destroy_labels(csv_data=params.csv_path, percents=10)-> None:
    if exists(csv_data):
        df = pd.read_csv(csv_data)
    train_df=df[df[params.csv_cols[6]]=='train']
    validation_df=df[df[params.csv_cols[6]]=='validation']
    test_df=df[df[params.csv_cols[6]]=='test']
    train_df = train_df.sample(frac=1).reset_index(drop=True)
    train_df_len = len(train_df.index)
    df_len_percents=int(train_df_len*(percents/100))
    train_df_percents=train_df[:df_len_percents]
    # print(train_df[params.csv_cols[4]])
    train_df_percents[[params.csv_cols[4]]] = np.random.permutation(train_df_percents[[params.csv_cols[4]]].values)
    # print(train_df[params.csv_cols[4]])
    final_df=train_df_percents.append(train_df[df_len_percents:]).append(validation_df).append(test_df)
    print(final_df)
    final_df.to_csv(params.destroy_label_csv_path, index=False)


def train_validate_test_split(csv_data=params.csv_path, train_percent=0.6, validate_percent=0.1, seed=None) ->pd.DataFrame:
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


if __name__ == '__main__':
     train_validate_test_split()
     # destroy_labels()
