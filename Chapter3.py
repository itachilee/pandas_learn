import pandas as pd

df = pd.read_csv('data/beijing_tianqi_2018.csv')

condition = df['ymd'].str.startswith('2018-03')


def get_nianyueri(x):
    year, month, day = x['ymd'].split("-")
    return f"{year}年{month}月{day}日"


df['中文日期'] = df.apply(get_nianyueri, axis=1)
print(
    df['中文日期']
)

print(df['中文日期'].str.replace('[年月日]', ''))
