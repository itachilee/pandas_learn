import pandas as pd
import numpy as np
fpath = 'data/beijing_tianqi_2018.csv'

df = pd.read_csv(fpath)

# 处理特殊字符℃
df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃', '').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃', '').astype('int32')

# 添加新列month
df['month'] = df['ymd'].str[:7]
# 每月最高温度
data = df.groupby('month')['bWendu'].max()

data.plot()

group_data = df.groupby('month').agg({'bWendu': np.max,'yWendu': np.min, 'aqi': np.mean})
print(
    group_data
)

group_data.plot()