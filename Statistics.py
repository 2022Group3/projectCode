#This file will show different statistics on our csv
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
        sns.countplot(x='label_name', data=typeDF)
        plt.show()

#
# if __name__ == '__main__':
#     st=Statistics(r"C:\פרוייקט בוטקמפ\projectCode\data.csv")
#     st.dataSize()
#     # st.distPerClass()
#     st.typeDistPerClass('test')