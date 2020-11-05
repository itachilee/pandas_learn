import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': list('abcde'), 'col2': range(5, 10), 'col3': [1.3, 2.5, 3.6, 4.6, 5.8]},
                  index=list('一二三四五'))
df = df.rename(index={'一': 'one'}, columns={'col1': 'new_col1'})

df1 = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
df2 = pd.DataFrame({'A': [1, 2, 3]}, index=[3, 1, 2])
print(df1)
print(df2)