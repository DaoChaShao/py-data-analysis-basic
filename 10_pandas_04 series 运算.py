import numpy as np
from pandas import Series
import random

"""
series 运算包括：聚合和广播
series 运算只有一维运算
聚合：sum(),min(),max(),mean(),median(),std(),var()
广播：add(),sub(),mul(),div(),pow()
"""


# 广播运算
def series_calculation_01():
    n = np.array([random.randint(0, 5) for _ in range(5)])
    """
    这个函数生成一个包含5个随机整数的数组，然后将每个元素加上4，并返回结果。
    :return: 数组和广播数组的对比
    """
    result = n + 4
    return f"原始数组：{n}，\n广播数组：{result}。"


def series_calculation_02():
    """
    这个函数生成了一个包含5个随机整数的Series，然后将每个元素加上4，并返回结果。
    :return:series和广播series的对比
    """
    s = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    s + 4
    return f"原始Series：\n{s}，\n广播Series：\n{s + 4}。"


def series_calculation_03():
    """
    这个函数生成了一个包含5个随机整数的Series，然后将每个元素加上数组，并返回结果。
    最终的结果是：隐式索引对齐
    :return:series和广播series的对比
    """
    s = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    n = np.ones(shape=5)
    cal = s + n
    return f"原始Series：\n{s}，\n数组列表：{n}，\n广播Series：\n{cal}。"


def series_calculation_04():
    """
    这个函数生成了一个包含5个随机整数的Series，series的value与二维数组相加，并返回结果。
    最终的结果是：np数组与数组的运算
    :return:series和广播series的对比
    """
    s = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    n = np.ones(shape=(2, 5))
    cal = s.values + n  # series的value与二维数组不能相加
    return f"原始Series：\n{s}，\nSeries的value:{s.values}，\n二位数组列表：{n}，\n广播Series：\n{cal}。"


def series_calculation_05():
    """
    这个函数生成两个series，然后将两个series相加，并返回结果。
    最终的结果是：两个series的显示索引对齐，且对齐后的索引值是两个series的并集，无法对齐的元素填充NaN
    :return:series和广播series的对比
    """
    s1 = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    s2 = Series(data=np.random.randint(0, 10, size=5), index=list("BCDEF"))
    cal = s1 + s2
    return f"原始Series1：\n{s1}，\n原始Series2：\n{s2}，\n广播Series：\n{cal}。"


def series_calculation_06():
    """
    这个函数生成两个series，然后将两个series相加，并返回结果。
    最终的结果是：两个series的显示索引对齐，且对齐后的索引值是两个series的并集，无法对齐的元素填充NaN
    :return:series和广播series的对比
    """
    s1 = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    s2 = Series(data=np.random.randint(0, 10, size=4), index=list("ABCD"))
    cal = s1 + s2
    return f"原始Series1：\n{s1}，\n原始Series2：\n{s2}，\n广播Series：\n{cal}。"


def series_calculation_07():
    """"""
    s1 = Series(data=np.random.randint(0, 10, size=5), index=list("ABCDE"))
    s2 = Series(data=np.random.randint(0, 10, size=4), index=list("ABCD"))
    s1.add(s2, fill_value=0)
    return f"原始Series1：\n{s1}，\n原始Series2：\n{s2}，\n填充0后的广播Series：\n{s1.add(s2, fill_value=0)}。"


if __name__ == "__main__":
    print(series_calculation_01())
    print(series_calculation_02())
    print(series_calculation_03())
    print(series_calculation_04())
    print(series_calculation_05())
    print(series_calculation_06())
    print(series_calculation_07())
