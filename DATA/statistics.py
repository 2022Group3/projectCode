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


def data_size():
    logging.info("data_size")
    print(len(df))


def dist_per_class():
    logging.info("dist_per_class")
    sns.countplot(x=params.csv_cols[4],data=df).set(title="classes of all data distribution")
    plt.xticks(rotation=90, ha='right')
    # sns.distplot(trainDF['label_name'])
    plt.tight_layout()
    plt.show()


def type_dist_per_class(type):
    logging.info("type_dist_per_class")
    type_df = df[df[params.csv_cols[6]] == type]
    if len(type_df) > 0:
        sns.countplot(x=params.csv_cols[4], data=type_df).set(title=type)
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print(f'{type} is empty')


def countplot_distribution_of_train_validation_test():
    logging.info("countplot_distribution_of_train_validation_test")
    sns.countplot(x=df[params.csv_cols[6]], data=df).set(title="train validation test distribution")
    plt.show()


def pie_distribution_of_train_validation_test(types, data):
    logging.info("pie_distribution_of_train_validation_test")
    # Creating explode data
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


def distribution_of_train_validation_test(distribution=True, pie=False):
    logging.info("distribution_of_train_validation_test")
    types = ['train', 'validation', 'test']
    types_size = [len(df[df[params.csv_cols[6]] == 'train']),
                  len(df[df[params.csv_cols[6]] == 'validation']),
                  len(df[df[params.csv_cols[6]] == 'test'])]

    if distribution:
        countplot_distribution_of_train_validation_test()
    if pie:
        pie_distribution_of_train_validation_test(types, types_size)


def stas():
    plt.figure(figsize=(12, 7), dpi=80)
    barWidth = 0.3

    df = create_data_csv.load_csv()
    train=[0]*(10+len(params.chosen_label))
    test = [0]*(10+len(params.chosen_label))
    validation = [0]*(10+len(params.chosen_label))
    for index, row in df.iterrows():
        if row['train/validation/test']=='train':
            train[row['current_label_number']] += 1
        if row['train/validation/test']=='test':
            test[row['current_label_number']]+=1
        if row['train/validation/test']=='validation':
            validation[row['current_label_number']]+=1

    # Set position of bar on X axis
    r1 = np.arange(len(train))
    r3 = [x + barWidth for x in r1]
    r2 = [x + barWidth for x in r3]


    # Make the plot
    plt.bar(r1, train, color='limegreen', width=barWidth, edgecolor='white', label='train')
    plt.bar(r3, test, color='deeppink', width=barWidth, edgecolor='white', label='test')
    plt.bar(r2, validation, color='cadetblue', width=barWidth, edgecolor='white', label='validation')
    # Add xticks on the middle of the group bars
    plt.xlabel('labels', fontweight='bold')
    labels=extract_images_from_pickle.get_labels_name()
    plt.xticks([r + barWidth for r in range(len(train))], labels)
    plt.xticks(rotation=90, ha='right')
    # sns.distplot(trainDF['label_name'])
    plt.tight_layout()

    # Create legend & Show graphic
    plt.legend()
    plt.show()


def show_all_statistics():
    logging.info("show_all_statistics")
    dist_per_class()
    type_dist_per_class('train')
    type_dist_per_class('validation')
    type_dist_per_class('test')
    distribution_of_train_validation_test(pie=True)
    stas()
if __name__ == '__main__':
    show_all_statistics()