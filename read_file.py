#!/usr/bin/python3
import pandas as pd

df = pd.read_csv('House Sales Values.csv')
print("houses.csv")
print(df.head(10))
print(df.shape)
print(df.dtypes)
print(df.describe())

