# This file shows different statistics on our data.csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import params
from matplotlib import pyplot
import seaborn

df = pd.read_csv(params.csv_path)


def data_size():
    print(len(df))


def dist_per_class():

    sns.countplot(x=params.csv_cols[4],data=df).set(title="classes of all data distribution")
    plt.xticks(rotation=90, ha='right')
    # sns.distplot(trainDF['label_name'])
    plt.tight_layout()
    plt.show()


def type_dist_per_class(type):
    type_df = df[df[params.csv_cols[6]] == type]
    if len(type_df) > 0:
        sns.countplot(x=params.csv_cols[4], data=type_df).set(title=type)
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print(f'{type} is empty')


def countplot_distribution_of_train_validation_test():
    sns.countplot(x=df[params.csv_cols[6]], data=df).set(title="train validation test distribution")
    plt.show()


def pie_distribution_of_train_validation_test(types, data):
    # Creating explode data
    explode = (0.1, 0.0, 0.2)

    # Creating color parameters
    colors = ("orange", "cyan", "brown")

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
    # Creating dataset
    types = ['train', 'validation', 'test']
    types_size = [len(df[df[params.csv_cols[6]] == 'train']),
                  len(df[df[params.csv_cols[6]] == 'validation']),
                  len(df[df[params.csv_cols[6]] == 'test'])]

    if distribution:
        countplot_distribution_of_train_validation_test()
    if pie:
        pie_distribution_of_train_validation_test(types, types_size)


def show_all_statistics():
    dist_per_class()
    type_dist_per_class('train')
    type_dist_per_class('validation')
    type_dist_per_class('test')
    distribution_of_train_validation_test(pie=True)
