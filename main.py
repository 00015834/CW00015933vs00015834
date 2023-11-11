#Reading dataset
import pandas as pd
import matplotlib.pyplot as pltpip
import os

df = pd.read_csv(r"data.csv")
print(df)

# #Data exploration
# #1) number of rows and columns
num_rows, num_columns = df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

#2)available features (column names)
features = df.columns.tolist()
print("Available features:")
print(features)

#3)display summary information
# print(df.info())

#DATA Cleaning
#drop a column(Reading frequency.1)
df= df.drop('Reading frequency.1', axis =1)
print(df)

#checking if columns renamed or not
features = df.columns.tolist()
print("Available features:")
print(features)

#Rename columns
df = df.rename(columns={'COURSE ID': 'Course ID', 'GRADE':'Grade', 'STUDENT ID': 'Student ID' })
print(df)

#checking if any data is duplicated
df = df.loc[df.duplicated()]
print(df)

#Grouping data
# g = df.groupby('GRADE')
# print(g)
#
# for GRADE, GRADE_df in g:
#     print(GRADE)
#     print(GRADE_df)


#calculating average columns









