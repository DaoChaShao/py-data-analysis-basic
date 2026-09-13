
import numpy as np
from pandas import Series, DataFrame
from faker import Faker
import random

from utils import countdown, lines

"""
NaN 是浮点数的一种特殊值，它表示“Not a Number”，即“非数字”或“无效数值”。
NaN 不是一个变量，也不能参与运算。
"""


@countdown
def print_nan():
    """输出NaN的类型"""
    nan = np.nan
    print(nan)
    lines()
    nan_type = type(nan)
    print(nan_type)
    return nan, nan_type


@countdown
def cal_nan():
    """计算NaN"""
    nan = np.nan
    nan_result = nan + 1
    print(nan_result)


@countdown
def cal_np_nan():
    """把arr中的某个元素替换为None"""
    arr_min = 1
    arr_max = 10
    series_size = 5
    arr = Series(data=np.random.randint(arr_min, arr_max, size=series_size))
    print(arr)
    lines()
    # 随机把arr中的某个元素替换为None
    arr[random.randint(0, series_size-1)] = None
    print(arr)


# @cds.decorator_beautification
def cal_df_nan():
    """计算DataFrame中的NaN"""
    s_min = 0
    s_max = 100
    s_size_row = 3
    s_size_col = 5
    index_name = ["Tom", "John", "Smith"]
    subjects = ["Chinese", "English", "Mathmatics", "Physics", "Chemistry", "Biology", "History", "Geography", "Politics"]
    s_col = random.sample(
        subjects,  # 科目列表
        k=min(s_size_col, len(subjects))  # 选择 s_size_col 和 subjects 列表长度中较小的那个数目，以确保不会超出 subjects 列表中的范围
    )
    df = DataFrame(data=np.random.randint(s_min, s_max, size=(s_size_row, s_size_col)), index=index_name, columns=s_col)
    # print(df)
    # cbu.draw_lines()
    # print(f"类型：{df.dtypes}")
    # cbu.draw_lines()
    df.iloc[random.randint(0, s_size_row-1), random.randint(0, s_size_col-1)] = None
    print(df)
    # cbu.draw_lines()
    # print(f"类型：{df.dtypes}")
    return df


@countdown
def check_nan():
    """检查NaN"""
    df = cal_df_nan()
    lines()
    print(f"df整体查询nan的结果：\n{df.isnull()}")
    lines()
    print(f"df每行总体查询nan的结果：\n{df.isnull().any(axis=1)}")  # 任何一行有nan，则为True
    lines()
    print(f"df每行总体查询nan的结果：\n{df.notnull().all(axis=1)}")  # 任何一行有nan，则为False，与isnull()相反
    lines()
    print(f"df每列总体查询nan的结果：\n{df.isnull().any(axis=0)}")
    lines()
    print(f"df每列总体查询nan的结果：\n{df.notnull().all(axis=0)}")  # 任何一行有nan，则为False，与isnull()相反


@countdown
def df_filter_nan():
    """过滤DataFrame中的NaN"""
    df = cal_df_nan()
    lines()
    print(f"df过滤nan的结果：\n{df.dropna(axis=0)}")  # 过滤掉所有含有nan的行 ，默认删除行数据
    lines()
    print(f"df过滤nan的结果：\n{df.dropna(axis=1)}")  # 过滤掉所有含有nan的列 ，默认删除列数据
    lines()
    print(f"df过滤nan的结果：\n{df.dropna(axis=0, how='all')}")  # 过滤掉所有含有nan的行和列，all是整行或列都是nan才会删掉


@countdown
def df_fill_nan_01():
    """填充DataFrame中的NaN"""
    df = cal_df_nan()
    lines()
    print(f"df填充nan的结果：\n{df.fillna(value=0)}")  # 填充nan为0


@countdown
def df_fill_nan_02():
    """填充DataFrame中的NaN"""
    data_len = 10
    index_col = ["Height", "Weight", "Age"]
    index_row = [Faker().name() for _ in range(data_len)]
    fake_dict = {
        index_col[0]: [random.randint(150, 200) for _ in range(data_len)],
        index_col[1]: [random.randint(40, 60) for _ in range(data_len)],
        index_col[2]: [random.randint(18, 30) for _ in range(data_len)]
    }
    df = DataFrame(fake_dict, index=index_row, columns=index_col)
    print(df)
    lines()
    # 随机生成3个 NaN
    for i in range(len(index_col)):
        df.iloc[random.randint(0, data_len-1), random.randint(0, df.shape[1]-1)] = None
    print(df)
    # 通常使用每列的聚合指标（均值）进行 NaN 值的填充
    lines()
    # 获得列均值
    col_mean = round(df.mean(axis=0), 2)
    print(f"列均值：\n{col_mean}")
    lines()
    # 填充 NaN 值
    df.fillna(value=col_mean, inplace=True)  # inplace=True 表示直接修改原 DataFrame
    print(df)


@countdown
def df_fill_nan_03():
    """填充DataFrame中的NaN"""
    data_len = 10
    index_col = ["Height", "Weight", "Age"]
    index_row = [Faker().name() for _ in range(data_len)]
    fake_dict = {
        index_col[0]: [random.randint(150, 200) for _ in range(data_len)],
        index_col[1]: [random.randint(40, 60) for _ in range(data_len)],
        index_col[2]: [random.randint(18, 30) for _ in range(data_len)]
    }
    df = DataFrame(fake_dict, index=index_row, columns=index_col)
    print(df)
    lines()
    # 随机生成3个 NaN
    for i in range(len(index_col)):
        df.iloc[random.randint(0, data_len-1), random.randint(0, df.shape[1]-1)] = None
    print(df)
    lines()
    # 使用相邻值进行 NaN 值的填充
    # df.ffill(axis=0, inplace=True)  # 向前填充，如果是列（axis=0），就用上一列的值填充本列的 NaN 值
    df.bfill(axis=0, inplace=True)  # 向后填充，如果是列（axis=0），就用下一列的值填充本列的 NaN 值
    # df.ffill(axis=1, inplace=True)  # 向前填充，如果是行（axis=1），就用上一行的值填充本行的 NaN 值。无值会报错
    # df.bfill(axis=1, inplace=True)  # 向后填充，如果是行（axis=1），就用下一行的值填充本行的 NaN 值。无值会报错
    print(df)


if __name__ == '__main__':
    print_nan()
    cal_nan()
    cal_np_nan()
    cal_df_nan()
    check_nan()
    df_filter_nan()
    df_fill_nan_01()
    df_fill_nan_02()
    df_fill_nan_03()