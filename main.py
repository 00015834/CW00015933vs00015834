#Reading dataset
import pandas as pd
import matplotlib.pyplot as pltpip
import os

df = pd.read_csv(r"data.csv")
print(df)

#Data exploration
#1) number of rows and columns
num_rows, num_columns = df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

#2)available features (column names)
features = df.columns.tolist()
print("Available features:")
print(features)

#3)display summary information
print(df.info())

#Data Cleaning
#drop a column




#Grouping data
g = df.groupby('GRADE')
print(g)

for GRADE, GRADE_df in g:
    print(GRADE)
    print(GRADE_df)


#d)







