#This file will show different statistics on our csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Statistics:
    def __init__(self,csv):
        self.df = pd.read_csv(csv)
        # print (self.df)

    def dataSize(self):
        print(len(self.df))

    def distPerClass(self):
        sns.countplot(x='label_name', data=self.df)
        # sns.distplot(trainDF['label_name'])
        plt.show()

    def typeDistPerClass(self, type):
        typeDF=self.df[self.df['train/validation/test']==type]
        if(len(typeDF)>0):
            sns.countplot(x='label_name', data=typeDF)
            plt.show()
        else:
            print(type +' is empty')

    def countplot_distribution_of_train_validation_test(self):
        sns.countplot(x=self.df['train/validation/test'],data=self.df)
        plt.show()

    def pie_distribution_of_train_validation_test(self,types,data):
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
    def distribution_of_train_validation_test(self,distribution=True,pie=False):
        # Creating dataset
        types = ['train','validation','test']
        data=[len(self.df[self.df['train/validation/test']=='train']),
        len(self.df[self.df['train/validation/test']=='validation']),
        len(self.df[self.df['train/validation/test']=='test'])]
        if distribution==True:
            self.countplot_distribution_of_train_validation_test()
        if pie==True:
            self.pie_distribution_of_train_validation_test(types, data)




if __name__ == '__main__':
    st=Statistics(r"C:\D\bootcamp\project\projectCode\df.csv")
    # st.dataSize()
    st.distPerClass()
    st.typeDistPerClass('train')
    st.typeDistPerClass('validation')
    st.typeDistPerClass('test')
    # print(len(st.df[st.df['train/validation/test']=='train']))
    st.distribution_of_train_validation_test(pie=True)
