import numpy as np
import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines

"""
pandas 的级联分为：
1.级联：pd.concat(), pd.append()
2.合并：pd.merge()
"""


def create_numpy():
    """创建numpy数组"""
    np_random_min = 0
    np_random_max = 100
    arr_01 = np.random.randint(np_random_min, np_random_max, size=(2, 3))
    arr_02 = np.random.randint(np_random_min, np_random_max, size=(4, 3))
    print(arr_01)
    lines()
    print(arr_02)
    return arr_01, arr_02


@countdown
def numpy_combine():
    """numpy 的级联在形状上要保持一致"""
    arr_01, arr_02 = create_numpy()
    lines()
    new_arr = np.concatenate((arr_01, arr_02), axis=0)  # 按行级联，但因为列形状不一致，所以无法按列级联
    print(new_arr)


def create_dataframe():
    """创建 2 个 col 一致的 pandas DataFrame"""
    data_row = 5
    data_col = 3
    score_min = 0
    score_max = 100
    index_name_01 = [Faker().first_name() for _ in range(data_row)]
    subs = [
        "Chinese", "Math", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics"
    ]
    random_subs = (random.sample(subs, k=min(data_col, len(subs))))
    df_dict_01 = {
        subject_01: [random.randint(score_min, score_max) for _ in range(data_row)]
        for subject_01 in random_subs
    }
    df_01 = DataFrame(df_dict_01, index=index_name_01, columns=random_subs)
    print(df_01)
    print(df_01.shape)

    lines()
    data_row = 7
    index_name_02 = [Faker().first_name() for _ in range(data_row)]
    # 增加3行数据
    df_dict_02 = {
        subject_02: [random.randint(score_min, score_max) for _ in range(data_row)]
        for subject_02 in random_subs
    }
    df_02 = DataFrame(df_dict_02, index=index_name_02, columns=random_subs)
    print(df_02)
    print(df_02.shape)
    return df_01, df_02


@countdown
def df_combine():
    """pandas 的级联"""
    df_01, df_02 = create_dataframe()
    lines()
    df = pd.concat((df_01, df_02), axis=0)
    # 行级联
    print(f"行级联结果：\n{df}")
    print(df.shape)

    lines()

    # 列级联
    df = pd.concat((df_01, df_02), axis=1)
    print(f"列级联结果：\n{df}")
    print(df.shape)


@countdown
def ignore_index():
    """ignore_index 参数"""
    cols = ["Chinese", "Math", "English"]
    df_01 = DataFrame(data=np.random.randint(0, 100, size=(3, 3)), columns=cols)
    df_02 = DataFrame(data=np.random.randint(0, 100, size=(5, 3)), columns=cols)
    print(df_01)
    print(df_01.shape)
    lines()
    print(df_02)
    print(df_02.shape)
    lines()
    df = pd.concat((df_01, df_02), axis=0, ignore_index=True)  # 如果原索引无意义，忽略原始索引，避免重复
    print(f"ignore_index=True 结果：\n{df}")
    print(df.shape)


@countdown
def concat_keys():
    """concat_keys 参数"""
    cols = ["Chinese", "Math", "English"]
    df_01 = DataFrame(data=np.random.randint(0, 100, size=(3, 3)), columns=cols)
    df_02 = DataFrame(data=np.random.randint(0, 100, size=(5, 3)), columns=cols)
    print(df_01)
    print(df_01.shape)
    lines()
    print(df_02)
    print(df_02.shape)
    lines()
    df = pd.concat((df_01, df_02), axis=1, keys=["middle term", "final term"])  # 给不同 DataFrame 加上索引
    print(f"concat_keys 结果：\n{df}")


@countdown
def concat_example():
    """concat 示例"""
    data_row = 5
    data_col = 3
    score_min = 0
    score_max = 100
    index_name = [Faker().first_name() for _ in range(data_row)]
    subs = [
        "Chinese", "Math", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    random_subs = (random.sample(subs, k=min(data_col, len(subs))))
    df_dict = {
        sub: [random.randint(score_min, score_max) for _ in range(data_row)]
        for sub in random_subs
    }
    df = DataFrame(data=df_dict, index=index_name, columns=random_subs)
    print(df)
    print(df.shape)
    lines()
    # 列练级，添加一列
    new_col_df = DataFrame(
        data=np.random.randint(0, 100, size=(data_row, 1)),
        columns=["Computer"],
        index=index_name  # 行索引要保持一致
    )
    print(new_col_df)
    print(new_col_df.shape)
    lines()
    df = pd.concat((df, new_col_df), axis=1)  # 列级联
    print(df)
    print(df.shape)
    lines()
    # 行级联，添加一行新人和新成绩
    new_row_df = DataFrame(
        data=np.random.randint(0, 100, size=(1, (data_col + 1))),
        index=["New Person"],
        columns=random_subs + ["Computer"]  # 列索引要保持一致
    )
    df = pd.concat((df, new_row_df), axis=0)  # 行级联
    print(df)
    print(df.shape)


@countdown
def merge_example():
    """merge 示例"""
    score_min = 0
    score_max = 100
    subs = [
        "Chinese", "Math", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]

    data_row_01 = 5
    data_col_01 = 2
    index_name_01 = [Faker().first_name() for _ in range(data_row_01)]
    random_subs_01 = (random.sample(subs, k=min(data_col_01, len(subs))))
    df_dict_01 = {
        subject_01: [random.randint(score_min, score_max) for _ in range(data_row_01)]
        for subject_01 in random_subs_01
    }
    df_01 = DataFrame(df_dict_01, index=index_name_01, columns=random_subs_01)
    print(df_01)
    print(df_01.shape)

    lines()

    data_row_02 = 5
    data_col_02 = 4
    index_name_02 = [Faker().first_name() for _ in range(data_row_02)]
    random_subs_02 = (random.sample(subs, k=min(data_col_02, len(subs))))
    df_dict_02 = {
        subject_02: [random.randint(score_min, score_max) for _ in range(data_row_02)]
        for subject_02 in random_subs_02
    }
    df_02 = DataFrame(df_dict_02, index=index_name_02, columns=random_subs_02)
    print(df_02)
    print(df_02.shape)

    lines()

    # 内合并，即外连接：outer，保留所有字段，空值补NaN
    df = pd.concat([df_01, df_02], join='outer')
    print(f"内合并结果：\n{df}")
    print(df.shape)

    lines()

    # 填充空值
    df = df.fillna(value=df.mean(axis=0))
    print(f"填充空值结果：\n{df}")
    print(df.shape)

    lines()

    # 外合并，即外连接：inner，保留公共字段，会丢失原始数据
    df = pd.concat([df_01, df_02], join='inner')
    print(f"外合并结果：\n{df}")
    print(df.shape)


if __name__ == '__main__':
    create_numpy()
    numpy_combine()
    create_dataframe()
    df_combine()
    ignore_index()
    concat_keys()
    concat_example()
    merge_example()
