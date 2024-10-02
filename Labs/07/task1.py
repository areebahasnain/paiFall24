import pandas as pd

df = pd.read_csv('heartDisease.csv')
pd.set_option('display.max_rows', None)
filtered_df = df[df['ca'] == 2]
print(filtered_df)
