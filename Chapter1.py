import pandas as pd
import numpy as np

df = pd.read_csv('data/Game_of_Thrones_Script.csv')

df['Name'].nunique()
print(df['Name'].value_counts())
print('-------')
print(df['Name'].value_counts().index[0])
print('-------')
df_words = df.assign(Words=df['Sentence'].apply(lambda x:len(x.split()))).sort_values(by='Name')

print(df_words.head())