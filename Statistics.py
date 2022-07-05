#This file will show different statistics on our csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file=r"C:\Users\אפרת\Downloads\df.csv"
df =pd.read_csv(file)

def dataSize():
    print(len(df))

def distPerClass():
    sns.countplot(x='label_name', data=df)
    # sns.distplot(trainDF['label_name'])
    plt.show()

def typeDistPerClass(type):
    typeDF=df[df['train/validation/test']==type]
    if(len(typeDF)>0):
        sns.countplot(x='label_name', data=typeDF)
        plt.show()
    else:
        print(type +' is empty')

def countplot_distribution_of_train_validation_test():
    sns.countplot(x=df['train/validation/test'],data=df)
    plt.show()

def pie_distribution_of_train_validation_test(types,data):
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
    wedges, texts, autotexts = ax.pie(data,
                                        autopct=lambda pct: func(pct, data),
                                        explode=explode,
                                        labels=types,
                                        shadow=True,
                                        colors=colors,
                                        startangle=90,
                                        wedgeprops=wp,
                                        textprops=dict(color="magenta"))
    # Adding legend
    ax.legend(wedges, types,
                title="types",
                loc="center left",
                bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")
    ax.set_title("train validation test distribution")

    # show plot
    plt.show()
def distribution_of_train_validation_test(distribution=True,pie=False):
    # Creating dataset
    types = ['train','validation','test']
    data=[len(df[df['train/validation/test']=='train']),
    len(df[df['train/validation/test']=='validation']),
    len(df[df['train/validation/test']=='test'])]
    if distribution==True:
        countplot_distribution_of_train_validation_test()
    if pie==True:
        pie_distribution_of_train_validation_test(types, data)




if __name__ == '__main__':
    distPerClass()
    typeDistPerClass('train')
    typeDistPerClass('validation')
    typeDistPerClass('test')
    # print(len(st.df[st.df['train/validation/test']=='train']))
    distribution_of_train_validation_test(pie=True)
