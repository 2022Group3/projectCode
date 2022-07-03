#This file will show different statistics on our csv
import pandas as pd

class Statistics:
    def __init__(self,csv):
        self.df = pd.read_csv(csv)
        print (self.df)

    def dataSize(self):
        print(len(self.df))

if __name__ == '__main__':
    st=Statistics(r"C:\פרוייקט בוטקמפ\projectCode\data.csv")

    st.dataSize()