import pandas as pd

df = pd.read_csv('iris.csv')
df_trimmed = df.iloc[:-50]
df_trimmed.to_csv('iris.csv', index=False)
