import logging

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os.path import exists
import params
from DATA import create_data_csv, extract_images_from_pickle
import numpy as np

if exists(params.csv_path):
    df = pd.read_csv(params.csv_path)
else:
    df = pd.DataFrame()


def dist_per_class() -> None:
    """
    show distribution per class
    :return:
    """
    logging.info("dist_per_class")
    sns.countplot(x=params.csv_cols[4], data=df).set(title="classes of all data distribution")
    plt.xticks(rotation=90, ha='right')
    # sns.distplot(trainDF['label_name'])
    plt.tight_layout()
    plt.show()


def type_dist_per_class(type:str)->None:
    '''
    show distribution per class for the type of the data :train / test / validation
    :param type: train / test / validation
    :return:
    '''
    logging.info("type_dist_per_class")
    type_df = df[df[params.csv_cols[6]] == type]
    if len(type_df) > 0:
        sns.countplot(x=params.csv_cols[4], data=type_df).set(title=type)
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print(f'{type} is empty')


def countplot_distribution_of_train_validation_test()->None:
    '''
    show countplot distribution of train validation and test
    :return:
    '''
    logging.info("countplot_distribution_of_train_validation_test")
    sns.countplot(x=df[params.csv_cols[6]], data=df).set(title="train validation test distribution")
    plt.show()


def pie_distribution_of_train_validation_test(types:list, data:list[str])->None:
    '''
    show distribution in pie shape for train test and validation
    :param types: train,validation, test
    :param data: count in each part
    :return:
    '''
    logging.info("pie_distribution_of_train_validation_test")
    explode = (0.1, 0.0, 0.2)

    # Creating color parameters
    colors = ("limegreen", "deeppink", "cadetblue")

    # Wedge properties
    wp = {'linewidth': 1, 'edgecolor': "green"}

    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)

        # Creating plot

    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data), explode=explode, labels=types,
                                      shadow=True, colors=colors, startangle=90, wedgeprops=wp,
                                      textprops=dict(color="magenta"))
    # Adding legend
    ax.legend(wedges, types, title="types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("train validation test distribution")

    # show plot
    plt.show()


def distribution_of_train_validation_test(distribution=True, pie=False) -> None:
    """
    display distribution of the train validation test
    :param distribution:
    :param pie: if show also the pie distribution
    :return:
    """
    logging.info("distribution_of_train_validation_test")
    types = ['train', 'validation', 'test']
    types_size = [len(df[df[params.csv_cols[6]] == 'train']),
                  len(df[df[params.csv_cols[6]] == 'validation']),
                  len(df[df[params.csv_cols[6]] == 'test'])]

    if distribution:
        countplot_distribution_of_train_validation_test()
    if pie:
        pie_distribution_of_train_validation_test(types, types_size)


def statistic_together() -> None:
    """
    display plot of the division distribution
    :return:None
    """
    logging.info("statistic_together")
    plt.figure(figsize=(12, 7), dpi=80)
    bar_width = 0.3
    df_csv = create_data_csv.load_csv()
    train = [0] * (10 + len(params.chosen_label))
    test = [0] * (10 + len(params.chosen_label))
    validation = [0] * (10 + len(params.chosen_label))
    for index, row in df_csv.iterrows():
        if row['train/validation/test'] == 'train':
            train[row['current_label_number']] += 1
        if row['train/validation/test'] == 'test':
            test[row['current_label_number']] += 1
        if row['train/validation/test'] == 'validation':
            validation[row['current_label_number']] += 1
    train_r = np.arange(len(train))
    test_r = [x + bar_width for x in train_r]
    validation_r = [x + bar_width for x in test_r]
    plt.bar(train_r, train, color='limegreen', width=bar_width, edgecolor='white', label='train')
    plt.bar(test_r, test, color='deeppink', width=bar_width, edgecolor='white', label='test')
    plt.bar(validation_r, validation, color='cadetblue', width=bar_width, edgecolor='white', label='validation')
    plt.xlabel('labels', fontweight='bold')
    labels = extract_images_from_pickle.get_labels_name()
    plt.xticks([r + bar_width for r in range(len(train))], labels)
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.legend()
    plt.show()


def show_all_statistics() -> None:
    """
    display the statistic of all the data separated to train, validation and tests
    :return: None
    """
    logging.info("show_all_statistics")
    dist_per_class()
    type_dist_per_class('train')
    type_dist_per_class('validation')
    type_dist_per_class('test')
    distribution_of_train_validation_test(pie=True)
    statistic_together()

if __name__ == '__main__':
    show_all_statistics()