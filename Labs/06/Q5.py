import pandas as pd

df = pd.read_csv("world_alcohol_consumption.csv")
print("Dimensions (Rows, Columns):", df.shape)
print("Column names:", df.columns.tolist())
