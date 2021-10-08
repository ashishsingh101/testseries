import pandas as pd
import numpy as np

class Csv_tojs:
    def csv_tojson(self,csv_data):
        jsonfilename=self.csv_data.join(".json")
        return(jsonfilename)


dataframe=self.pd.read_csv(csv_data)
csv_file='ireoluwa.csv'
okis=dataframe.csv_tojson(csv_file)
print(okis)