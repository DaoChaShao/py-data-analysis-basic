"""
dataframe 构造
dataframe 是一个有行有列的二维数据结构，可以用来存储和处理表格数据。
dataframe 有行索引，也有列索引。
dataframe 是Series的字典，字典的key就是二维表格的列索引。字典的值通常是一维数组。

"""

import numpy as np
import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines


@countdown
def create_dataframe():
    """创建dataframe"""
    # 一般方法
    date_frame_simple = DataFrame(
        np.random.randint(0, 100, size=(3, 5)),
        index=list("abc"),  # 行索引
        columns=list("ABCDE"),  # 列索引
    )
    print(date_frame_simple)
    # 字典方法
    # 设置列索引及其内容
    dict_method = {
        "A": np.random.randint(0, 100, size=3),
        "B": np.random.randint(0, 100, size=3),
        "C": np.random.randint(0, 100, size=3),
        "D": np.random.randint(0, 100, size=3),
        "E": np.random.randint(0, 100, size=3),
    }
    data_frame_dict = DataFrame(dict_method, index=list("abc"))
    print(data_frame_dict)
    return data_frame_dict


def normal_dataframe():
    """用字典方式创建常见dataframe"""
    # 数据条数
    num_row = 10
    # 创建多类型字典数据
    fake_dict = {
        "Name": [Faker().last_name() for _ in range(num_row)],
        "Age": [random.randint(18, 60) for _ in range(num_row)],
        "Gender": [random.choice(["Male", "Female"]) for _ in range(num_row)],
        "Occupation": [Faker().job() for _ in range(num_row)],
        "Salary": [random.randint(5000, 10000) for _ in range(num_row)],
        "KPI": [random.randint(0, 100) for _ in range(num_row)],
    }
    fake_data_frame = DataFrame(fake_dict, index=list([num + 1 for num in range(num_row)]))
    # print(fake_data_frame)
    return fake_data_frame


def write_dataframe_to_excel():
    """将dataframe写入excel文件，但必须先安装openpyxl模块（pip3 install openpyxl）"""
    data_frame = normal_dataframe()
    excel_path = "data/dataframe.xlsx"
    data_frame.to_excel(
        excel_path,  # 写入文件路径
        # sheet_name="sheet1",  # 写入文件标签
        index=False  # 不写入列索引
    )
    print("数据已写入excel文件：", excel_path)


"""
读取dataframe数据的方法：
1.read_csv()：读取csv文件
2.read_excel()：读取excel文件
3.read_sql()：读取数据库中的数据
4.read_html()：读取网页中的数据
5.read_json()：读取json文件
6.read_table():读取txt文件
"""


@countdown
def read_dataframe_from_excel():
    """读取excel文件中的dataframe"""
    excel_path = "data/dataframe.xlsx"
    data_frame_read = pd.read_excel(
        excel_path,
        sheet_name=0,  # 读取文件标签，默认第一个标签，或者传入标签名称
        header=0,  # 读取行标签，默认第一行
        index_col=0,  # 读取列标签，默认第一列
    )
    # 读取excel文件内容
    print(data_frame_read)
    lines()
    print("数据已读取excel文件：", excel_path)
    lines()
    # 保存读取的数据新excel文件
    data_frame_read.to_excel(
        "data/dataframe_read2save.xlsx",
        sheet_name="sheet1",  # 写入文件标签
        index=True,  # 写入列索引
    )
    print("数据已写入新excel文件：", "data/dataframe_read2save.xlsx")


if __name__ == '__main__':
    create_dataframe()
    normal_dataframe()
    write_dataframe_to_excel()  # 连续调用，需要关闭GUI装饰器
    read_dataframe_from_excel()
