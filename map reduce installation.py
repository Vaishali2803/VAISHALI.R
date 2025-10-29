import pandas as pd
import numpy as np
import sklearn
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target
print("First 5 records:")
print(df.head())
print("\nLast 5 records:")
print(df.tail())
print("\nDataset Info:")
df.info()
print("\nColumn Names:")
print(df.columns)
print("\nStatistical Summary:")
print(df.describe())
print(f"\nDataset Shape: {df.shape}")
print("\nMissing Values:")
print(df.isnull().sum())
duplicate_count = df.duplicated().sum()
print(f"\nDuplicate Values: {duplicate_count}")
if duplicate_count > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates dropped.")
else:
    print("No duplicates to drop.")
