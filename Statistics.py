#This file will show different statistics on our csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Statistics:
    def __init__(self,csv):
        self.df = pd.read_csv(csv)
        print (self.df)

    def dataSize(self):
        print(len(self.df))

    def countplot_distribution_of_train_validation_test(self):
        sns.countplot(x='train/validation/test', data=self.df)
        plt.show()

    def probability_pie_distribution_of_train_validation_test(self,types,data):
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
        ax.set_title("train validation and test distribution")

        # show plot
        plt.show()


    def distribution_of_train_validation_test(self,distribution=True,pie_whith_probability=False):
        types = ['train', 'validation', 'test']
        data = [self.df['train/validation/test'][self.df['train/validation/test'] == 'train'].size,
                self.df['train/validation/test'][self.df['train/validation/test'] == 'validation'].size,
                self.df['train/validation/test'][self.df['train/validation/test'] == 'test'].size]
        if distribution==True:
            self.countplot_distribution_of_train_validation_test()
        if pie_whith_probability==True:
            self.probability_pie_distribution_of_train_validation_test(types,data)







if __name__ == '__main__':
    data=r"C:\D\bootcamp\project\projectCode\data.csv"
    st=Statistics(data)
    st.dataSize()
    # st.distribution_of_train_validation_test()
    #types = ['train', 'validation', 'test']
    #data = [st.df['train/validation/test'][st.df['train/validation/test'] == 'train'].size,
            #st.df['train/validation/test'][st.df['train/validation/test'] == 'validation'].size,
            #st.df['train/validation/test'][st.df['train/validation/test'] == 'test'].size]
    st.distribution_of_train_validation_test(pie_whith_probability=True)
