import numpy as np
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines


def create_df_01():
    """
    创建一个包含不完全重复的重复值的 DataFrame
    """
    random_min = 50
    random_max = 100
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Name", "Gender", "Age", "Chinese", "Math", "English", ]
    df_dict = {
        cols[0]: names,
        cols[1]: np.random.choice(["Male", "Female"], data_rows),
        cols[2]: [random.randint(18, 60) for _ in range(data_rows)],
        cols[3]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[4]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[5]: [random.randint(random_min, random_max) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")
    lines()
    print(f"数据类型：\n{df.dtypes}")

    return df


@countdown
def df_describe():
    """ 数据描述 """
    df = create_df_01()
    lines()
    print(f"数据描述：\n{df.describe()}")
    print(f"数据维度：{df.shape}")


@countdown
def df_head():
    """ 数据前 5 行 """
    df = create_df_01()
    lines()
    print(f"数据前几行：\n{df.head()}")
    print(f"数据维度：{df.shape}")


@countdown
def df_info():
    """ 数据信息 """
    df = create_df_01()
    lines()
    df.info()
    print(f"数据维度：{df.shape}")


@countdown
def std_detect_outliers_np():
    """
    用标准差来检测异常值（不符合正态分布），即偏离 3 倍的标准差的数值（丨data丨 > std * 3）
    """
    # 创建正态分布数据
    data = np.random.randn(3000)  # numpy 一维数组
    # 获取数据的标准差
    std = data.std()
    std_outlier = std * 3
    print(f"数据标准差：{std}\n三倍标准差：{std_outlier}")
    lines()
    # 获取数据的绝对值
    abs = np.abs(data)
    # 找出绝对值大于三倍标准差的数值
    bool_list = abs > std_outlier  # 比较结果会形成 bool 数组
    # 筛选异常值
    outliers = data[bool_list]
    print(f"异常值有 {len(outliers)} 个，分别为：\n{outliers}")


@countdown
def std_detect_outliers_df():
    """ 用标准差来检测异常值（不符合正态分布）"""
    data = np.random.randn(3000, 3)  # numpy 二维数组
    # 通过 numpy 数组创建 DataFrame 数组
    df = DataFrame(data=data, columns=["Yesterday", "Today", "Tomorrow"])
    # 获取数据的标准差
    std = df.std()
    std_outlier = std * 3
    print(f"数据标准差：\n{std}\n\n三倍标准差：\n{std_outlier}")
    lines()
    # 获取数据的绝对值
    abs = np.abs(df)
    # 找出绝对值大于三倍标准差的数值，由于都是df，所以可以直接比较，返回的是 bool 数组
    bool_list_outliers = (abs > std_outlier).any(axis=1)  # 任意一列有 True 即为异常值
    # 筛选异常值
    outliers = df[bool_list_outliers]
    print(f"异常值有 {len(outliers)} 个，分别为：\n{outliers}")

    lines()

    # 呈现想要保留的列
    bool_list_keep = (abs <= std_outlier).all(axis=1)  # 任意一列有 False 即为保留值
    df_keep = df[bool_list_keep]
    print(f"保留值有 {len(df_keep)} 个，分别为：\n{df_keep}")


@countdown
def xxx():
    """
    用离群点来检测异常值
    :return:
    """
    pass


if __name__ == "__main__":
    create_df_01()
    df_describe()
    df_head()
    df_info()
    std_detect_outliers_np()
    std_detect_outliers_df()
