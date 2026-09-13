
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
    cols = ["Name", "Gender", "Age", "Chinese", "Math", "English",]
    df_dict = {
        cols[0]: names,
        cols[1]: np.random.choice(["Male", "Female"], size=data_rows),
        cols[2]: [random.randint(18, 60) for _ in range(data_rows)],
        cols[3]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[4]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[5]: [random.randint(random_min, random_max) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def df_take_rows():
    """ df 行排序 """
    df = create_df_01()
    lines()
    # 行数据从新排列
    df = df.take([0, 1, 0, 1,], axis=0)
    print(f"行数据从新排列:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def df_take_cols():
    """ df 列排序 """
    df = create_df_01()
    lines()
    # 列数据从新排列
    df = df.take([0, 1, 0, 1,], axis=1)
    print(f"列数据从新排列:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def df_random_permutation():
    """ df 随机排序 """
    df = create_df_01()
    lines()
    # 行数据随机排列
    permutation_row_list = np.random.permutation(df.shape[0])
    permutation_col_list = np.random.permutation(df.shape[1])
    # 行数据随机排列
    df = df.take(permutation_row_list, axis=0)
    # 列数据随机排列，一般只随机排列行，列数据一般不随机排序
    df = df.take(permutation_col_list, axis=1)
    print(f"行数据随机排列:\n{df}")
    print(f"数据维度：{df.shape}")


def create_df_02():
    """
    创建一个包含不完全重复的重复值的 DataFrame
    """
    random_min = 50
    random_max = 100
    data_rows = 100
    names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Name", "Gender", "Age", "Chinese", "Math", "English",]
    df_dict = {
        cols[0]: names,
        cols[1]: np.random.choice(["Male", "Female"], size=data_rows),
        cols[2]: [random.randint(18, 60) for _ in range(data_rows)],
        cols[3]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[4]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[5]: [random.randint(random_min, random_max) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def df_random_sample():
    """ df 随机抽样 """
    df = create_df_02()
    lines()
    # 随机抽样 几 组数据
    random_choice = 5
    # 随机抽样方法一
    df = df.take(np.random.randint(0, df.shape[0], size=random_choice))
    print(f"随机抽样 {random_choice} 组数据:\n{df}")
    print(f"数据维度：{df.shape}")
    lines()
    # 随机抽样方法二
    frac_float = float(random_choice / df.shape[0])
    df = df.sample(frac=frac_float, replace=False)  # frac：抽样比例，replace:是否可以重复抽样
    print(f"随机抽样 {random_choice} 组数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == "__main__":
    create_df_01()
    df_take_rows()
    df_take_cols()
    df_random_permutation()
    create_df_02()
    df_random_sample()