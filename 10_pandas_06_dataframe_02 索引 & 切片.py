import numpy as np
from pandas import Series, DataFrame
from faker import Faker
import random

from utils import countdown, lines


@countdown
def cut_numpy_array():
    arr = np.random.randint(0, 100, size=(3, 5))
    print(arr)
    lines()
    # 切出第一行的数据
    arr_row = arr[0]
    print(arr_row)
    lines()
    # 切出第一行第二个数据
    arr_row_item = arr[0][1]
    print(arr_row_item)
    lines()
    # 切出前两行的数据
    arr_rows = arr[[0, 1]]
    print(arr_rows)
    lines()
    # 切出第一列的数据
    arr_col = arr[:, 0]
    print(arr_col)
    lines()
    # 切出前两列数据
    arr_cols = arr[:, [0, 1]]
    print(arr_cols)
    return arr, arr_row, arr_row_item, arr_rows, arr_col, arr_cols


@countdown
def crate_dataframe():
    fake_data_len = 10
    fake_dict = {
        "Name": [Faker().name() for _ in range(fake_data_len)],
        "Age": [random.randint(18, 65) for _ in range(fake_data_len)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(fake_data_len)],
        "Occupation": [Faker().job() for _ in range(fake_data_len)],
        "Salary": [random.randint(5000, 10000) for _ in range(fake_data_len)],
        "KPI": [random.randint(0, 100) for _ in range(fake_data_len)],
    }
    df = DataFrame(fake_dict, index=range(1, fake_data_len + 1))
    print(df)
    return df


@countdown
def cut_dataframe_col_with_dict_method():
    """用字典方式切片dataframe，访问列数据"""
    df = crate_dataframe()
    df_name = df["Name"]
    lines()
    print(f"字典方式切片行数据：\n{df_name}")


@countdown
def cut_dataframe_col_with_list_method():
    """用标签方式切片dataframe，访问列数据"""
    df = crate_dataframe()
    df_cut = df[["Name", "Age"]]
    lines()
    print(f"列表标签方式切片行数据：\n{df_cut}")


@countdown
def cut_dataframe_col():
    """显式索引切片dataframe的列数据"""
    df = crate_dataframe()
    df_col = df.loc[1]
    lines()
    print(f"显示索引切片dataframe的列数据：\n{df_col}")


@countdown
def cut_dataframe_col_default():
    """隐式索引切片dataframe的列数据"""
    df = crate_dataframe()
    df_col = df.iloc[[0, 1]]
    lines()
    print(f"隐式索引切片dataframe的列数据：\n{df_col}")


@countdown
def cut_dataframe_cols():
    """显式索引切片dataframe的多个列数据"""
    df = crate_dataframe()
    # df_cols = df[["Name", "Age", "Gender"]]  # 方法一
    df_cols = df.loc[:, "Name": "Gender"]  # 方法二
    lines()
    print(f"切片dataframe的多个列数据：\n{df_cols}")


@countdown
def cut_dataframe_cols_default():
    """隐式索引切片dataframe的多个列数据"""
    df = crate_dataframe()
    # df_cols = df.iloc[:, [0, 1, 2]]  # 方法一
    df_cols = df.iloc[:, 0:2]  # 方法二
    lines()
    print(f"切片dataframe的多个列数据：\n{df_cols}")


@countdown
def cut_dataframe_item():
    """显式索引切片dataframe的单个元素"""
    df = crate_dataframe()
    # 访问单个元素（参数：先行后列）
    df_item = df.loc[1, "Name"]
    lines()
    print(f"切片dataframe的单个元素：{df_item}")


@countdown
def cut_dataframe_item_default():
    """隐式索引切片dataframe的单个元素"""
    df = crate_dataframe()
    # 访问单个元素（参数：先行后列）
    df_item = df.iloc[0, 0]  # 直接访问
    lines()
    print(f"切片dataframe的单个元素：{df_item}")


@countdown
def direct_access_dataframe_item():
    """直接访问dataframe的单个元素"""
    df = crate_dataframe()
    lines()
    df.loc[1, "Name"] = "Tom"
    print(f"直接访问dataframe的单个元素的修改结果：\n{df}")


@countdown
def cut_dataframe_row():
    """显式索引切片dataframe的行数据"""
    df = crate_dataframe()
    df_row = df.loc[1:3]
    lines()
    print(f"切片dataframe的行数据：\n{df_row}")


@countdown
def cut_dataframe_row_default():
    """隐式索引切片dataframe的行数据"""
    df = crate_dataframe()
    df_row = df.iloc[0:3]
    lines()
    print(f"切片dataframe的行数据：\n{df_row}")


@countdown
def cut_dataframe_bool_row():
    """布尔索引切片dataframe的行数据"""
    df = crate_dataframe()
    lines()
    list_bool = [random.choice([True, False]) for _ in range(df.shape[0])]  # shape[行，列]返回行数和列数
    print(list_bool)
    lines()
    df_bool = df.loc[list_bool]
    print(f"布尔索引切片dataframe的行数据：\n{df_bool}")


@countdown
def cut_dataframe_bool_col():
    """布尔索引切片dataframe的列数据"""
    df = crate_dataframe()
    lines()
    list_bool = [random.choice([True, False]) for _ in range(df.shape[1])]  # shape[行，列]返回行数和列数
    print(list_bool)
    lines()
    df_bool = df.loc[:, list_bool]
    print(f"布尔索引切片dataframe的列数据：\n{df_bool}")


@countdown
def cut_dataframe_bool_row_series():
    """布尔series索引切片dataframe的行数据"""
    df = crate_dataframe()
    lines()
    series_index = [num for num in range(1, df.shape[0] + 1)]  # 获取行索引
    series_bool = Series(
        data=[random.choice([True, False]) for _ in range(df.shape[0])],
        index=series_index,
    )
    print(series_bool)
    lines()
    df_bool = df.loc[series_bool]
    print(f"布尔series索引切片dataframe的行数据：\n{df_bool}")


@countdown
def cut_dataframe_bool_col_series():
    """布尔series索引切片dataframe的列数据"""
    df = crate_dataframe()
    lines()
    series_index = df.columns.tolist()  # 获取列标签
    print(series_index)
    lines()
    series_bool = Series(
        data=[random.choice([True, False]) for _ in range(df.shape[1])],
        index=series_index,
    )
    print(series_bool)
    lines()
    df_bool = df.loc[:, series_bool]
    print(f"布尔series索引切片dataframe的列数据：\n{df_bool}")


if __name__ == '__main__':
    cut_numpy_array()
    crate_dataframe()
    cut_dataframe_col_with_dict_method()
    cut_dataframe_col_with_list_method()
    cut_dataframe_col()
    cut_dataframe_col_default()
    cut_dataframe_cols()
    cut_dataframe_cols_default()
    cut_dataframe_item()
    cut_dataframe_item_default()
    direct_access_dataframe_item()
    cut_dataframe_row()
    cut_dataframe_row_default()
    cut_dataframe_bool_row()
    cut_dataframe_bool_col()
    cut_dataframe_bool_row_series()
    cut_dataframe_bool_col_series()
