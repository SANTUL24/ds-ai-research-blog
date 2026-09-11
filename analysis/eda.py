import pandas as pd


# Load data
df = pd.read_csv("../data/model_data.csv")


# Basic dataset information
print("Dataset shape:")
print(df.shape)


print("\nColumns:")
print(df.columns.tolist())


print("\nMissing values:")
print(df.isnull().sum())


print("\nSummary statistics:")
print(df.describe())