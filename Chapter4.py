import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.arange(12).reshape(3, 4),
    columns=['A', 'B', 'C', 'D']
)
print(
    df
)

# print(
#     df.drop('A',axis=1)
# )

# print(
#     df.drop(1,axis=0)
# )
# 按列遍历 反直觉，
print(
    df.mean(axis=0)
)
# 按行遍历
print(
    df.mean(axis=1)
)


def get_sum_value(x):
    return x['A'] * x['B'] * x['C'] * x['C']


df['sum_value'] = df.apply(get_sum_value, axis=1)

print(
    df
)
