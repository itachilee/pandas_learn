import pandas as pd
import numpy as np

# 跳过开头两行数据
studf = pd.read_excel('data/student.xlsx', skiprows=2)

# 获取到所有分数不为空的值
studf.loc[studf['分数'].notnull(), :]
#  axis : {0 or 'index', 1 or 'columns'}, default 0
# 删除所有空列
studf.dropna(axis=0, how='all', inplace=True)
# 删除所有空行
studf.dropna(axis=1, how='all', inplace=True)
# 处理空值
studf.loc[:, '分数'] = studf['分数'].fillna(0)
# equals to 'studf=studf.fillna({'分数':0})'
# 自动填充姓名列 method='ffill'
studf.loc[:, '姓名'] = studf['姓名'].fillna(method='ffill')
# 保存文档
studf.to_excel('data/student_clean.xlsx', index=False)
