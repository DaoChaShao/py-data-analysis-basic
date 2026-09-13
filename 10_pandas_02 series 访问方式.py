import numpy as np
import pandas as pd
from faker import Faker

from utils import countdown

"""
练习：
使用多种方法创建一下series
语文：150
数学：150
英语：150
理综：300
"""


def create_series():
    """构造series"""
    series = pd.Series(data=[150, 150, 150, 300], index=["语文", "数学", "英语", "理综"])
    return series


def dict_to_series():
    """字典转换为series"""
    data = {
        "语文": 150,
        "数学": 150,
        "英语": 150,
        "理综": 300
    }
    series = pd.Series(data=data)
    return series


def series_cut():
    """构造series"""
    arr = np.random.permutation(100)[:5]  # 在0-99中，随机生成5个元素
    series = pd.Series(arr, index=[Faker().last_name() for _ in range(5)])
    return f"系列：{series}\n切片：{series.iloc[[0, 3]]}\n切片：{series.iloc[[0, 1, 1]]}"


def loc_series():  # loc是官方推荐的访问方式
    """loc访问series"""
    series = pd.Series(data=[150, 150, 150, 300], index=["语文", "数学", "英语", "理综"])
    return f"字典访问：\n{series["理综"]}\n专属访问：\n{series.loc["数学"]}\n多个访问：\n{series.loc[["数学", "数学", "理综"]]}"


def bool_series():
    """布尔索引series"""
    index = ["语文", "数学", "英语", "理综"]  # 如果使用系列布尔作为索引，索引必须对齐（顺序无所谓），如果使用list或者array，可以不一致
    series = pd.Series(data=[150, 150, 150, 300], index=index)
    series_bool = pd.Series(data=[True, False, True, False], index=index)
    result = series > 150
    return series[series_bool], result, series[result]


if __name__ == '__main__':
    print(create_series())
    print(dict_to_series())
    print(series_cut())
    print(loc_series())
    print(bool_series())
