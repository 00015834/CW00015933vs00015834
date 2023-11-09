import pandas as pd
import matplotlib.pyplot as pltpip
import os

df = pd.read_csv(r"data.csv")
print(df) #reading data


df.columns #names of columns
print(df.columns)

df['GRADE'].max() #finding max value in GRADE column
print(df['GRADE'].max())

df.max() #print max values in data
print(df.max())




