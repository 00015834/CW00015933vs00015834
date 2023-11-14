# Reading dataset
import pandas as pd
import numpy as np
import os

df = pd.read_csv(r"data.csv")
print(df)

# Data  exploration
# 1) number of rows and columns
num_rows, num_columns = df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

# 2)available features (column names)
features = df.columns.tolist()
print("Available features:")
print(features)

# 3)display summary information
print(df.info())

# DATA Cleaning
# drop a column(Reading frequency.1)
df = df.drop('Reading frequency.1', axis =1)
print(df.head())

# checking if columns renamed or not
features = df.columns.tolist()
print("Available features:")
print(features)

# Rename columns
df = df.rename(columns={'COURSE ID': 'Course ID', 'GRADE':'Grade', 'STUDENT ID': 'Student ID' })
print(df)


# Finding the min and max values of columns
df['Student ID'] = pd.to_numeric(df['Student ID'], errors='coerce').fillna(-1).astype(int)  # converting integers

col_max = df.max(axis=0)  # max values
print(col_max)

col_min = df.min(axis=0)  # min values
print(col_min)









