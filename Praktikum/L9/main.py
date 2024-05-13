# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

df = pd.read_csv("C:/Users/yogaa/OneDrive/Dokumen/SMT 4/Kecerdasan-Buatan/Praktikum/L9/car.csv")
print('\n\nprint(df.head())')
print(df.head())
print('\n\nprint(df.shape)')
print(df.shape)
print('\n\ndf.info()')
df.info()
print('\n\nprint(df.describe())')
print(df.describe())
print('\n\nprint(df.describe())')
print(df.columns.tolist())
print('\n\ndf.isnull().sum()')
print(df.isnull().sum())
print('\n\ndf.nunique()')
print(df.nunique())




