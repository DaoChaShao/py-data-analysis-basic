import numpy as np
import pandas as pd
from pandas import Series
from faker import Faker


# numpy array 提供了运算基础
# pandas 提供了业务逻辑的处理方法

# series 是类似于一维数组，可以理解为一列数据，可以有索引，可以有名称，是一维数组的强化版，增加了key-value字典式的访问机制
# dataframe 是二维数组，可以理解为多列数据，可以有索引，可以有名称


def list_to_series():
    """由列表构成series"""
    names = [Faker().last_name() for i in range(5)]
    series = Series(names)
    return series


def ny_to_series():
    """由numpy array构成series"""
    arr = np.ones(5)
    series = pd.Series(arr)
    return series


def dict_series():
    """构成字典式的series"""
    names = [Faker().last_name() for i in range(5)]
    # 设置显式索引。如果不设置显式索引，则使用隐式索引自动填充
    series = Series(names, index=["key01", "key02", "key03", "key04", "key05"])
    return series


def dict_to_series():
    """由字典构成series"""
    dict = {
        "k3": Faker().last_name(),
        "k5": Faker().last_name(),
        "k1": Faker().last_name(),
        "k2": Faker().last_name(),
        "k4": Faker().last_name()
    }
    series = Series(data=dict)
    return series


if __name__ == '__main__':
    print(list_to_series())
    print(ny_to_series())
    print(dict_series())
    print(dict_to_series())
