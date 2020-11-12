import pandas as pd
from numpy.core.defchararray import isdigit

# fpath = 'data/stocks/11-12.json'
#
# stocks = pd.read_json(fpath)
# stocks['每手金额'] = stocks['总成交金额'] / stocks['总手']
# del stocks['spider_name']
# del stocks['images']
#
# # stocks.to_excel('11-12.xlsx')
# print(
#     # stocks.head() .T.head(12)
#     stocks.index
# )

execl_path = '11-12.xlsx'

stocks = pd.read_excel(execl_path)
stocks.set_index('排名')


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False


def get_digit(x):
    return x if is_number(x) else 0


stocks['涨跌幅'] = stocks['涨跌幅'].apply(lambda x: x if is_number(x) else 0)

print(
    stocks['涨跌幅']
)
stocks.to_excel('text.xlsx')