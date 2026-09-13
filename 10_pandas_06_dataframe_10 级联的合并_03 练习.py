import pandas as pd
from pandas import DataFrame
import random

from utils import lines, countdown


def create_df_01():
    """创建列标签无差异 DataFrame"""
    rows = ["Chinese", "Maths", "English"]
    cols_3 = ["Tom", "John", "Smith"]
    scores_min = 0
    scores_max = 100
    random_scores = [random.randint(scores_min, scores_max) for _ in range(len(rows))]
    df_3_dict = {
        cols_3[0]: random_scores,
        cols_3[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
        cols_3[2]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_3 = DataFrame(df_3_dict, index=rows, columns=cols_3)
    print(df_3)
    print(df_3.shape)

    lines()

    cols_2 = ["Tom", "Jerry"]
    df_2_dict = {
        cols_2[0]: random_scores,
        cols_2[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_2 = DataFrame(df_2_dict, index=rows, columns=cols_2)
    print(df_2)
    print(df_2.shape)

    return df_3, df_2


@countdown
def merge_df_01():
    """合并 DataFrame"""
    df_3, df_2 = create_df_01()
    lines()
    df_merge = pd.merge(df_3, df_2)
    print(f"列标签一致的合并结果：\n{df_merge}")
    print(df_merge.shape)


def create_df_02():
    """创建列标签有差异的 DataFrame"""
    rows = ["Chinese", "Maths", "English"]
    cols_3 = ["Tom", "John", "Smith"]
    scores_min = 0
    scores_max = 100
    random_scores = [random.randint(scores_min, scores_max) for _ in range(len(rows))]
    df_3_dict = {
        cols_3[0]: random_scores,
        cols_3[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
        cols_3[2]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_3 = DataFrame(df_3_dict, index=rows, columns=cols_3)
    print(df_3)
    print(df_3.shape)

    lines()

    cols_2 = ["Tomy", "Jerry"]
    df_2_dict = {
        cols_2[0]: random_scores,
        cols_2[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_2 = DataFrame(df_2_dict, index=rows, columns=cols_2)
    print(df_2)
    print(df_2.shape)

    return df_3, df_2


@countdown
def merge_df_02():
    """合并列标签不一致的 DataFrame"""
    df_3, df_2 = create_df_02()
    lines()
    df_merge = pd.merge(df_3, df_2, left_index=True, right_index=True)  # 或者 left_on="Tom", right_on = "Tomy"
    print(f"列标签不同的合并结果：\n{df_merge}")
    print(df_merge.shape)

    lines()

    # 删除合并后重复的列
    df_drop = df_merge.drop(columns=["Tomy"])
    print(f"删除合并后重复的列：\n{df_drop}")
    print(df_drop.shape)


def create_df_03():
    """创建列标签一致，但数据有差异 DataFrame"""
    rows = ["Chinese", "Maths", "English"]
    cols_1 = ["Tom", "Jerry", ]
    scores_min = 0
    scores_max = 100
    random_scores = [random.randint(scores_min, scores_max) for _ in range(len(rows))]
    df_3_dict = {
        cols_1[0]: random_scores,
        cols_1[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_3 = DataFrame(df_3_dict, index=rows, columns=cols_1)
    print(df_3)
    print(df_3.shape)

    lines()

    cols_2 = ["Tom", "Jerry", "Smith"]
    df_2_dict = {
        cols_2[0]: random_scores,
        cols_2[1]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
        cols_2[2]: [random.randint(scores_min, scores_max) for _ in range(len(rows))],
    }
    df_2 = DataFrame(df_2_dict, index=rows, columns=cols_2)
    print(df_2)
    print(df_2.shape)

    return df_3, df_2


@countdown
def merge_df_03():
    """合并列标签一致，但数据有差异的 DataFrame"""
    df_3, df_2 = create_df_03()
    lines()
    df_merge = pd.merge(df_3, df_2, on="Tom", suffixes=("_Junior", "_Senior"))
    print(f"列标签一致，但数据有差异的合并结果：\n{df_merge}")
    print(df_merge.shape)


if __name__ == "__main__":
    create_df_01()
    merge_df_01()
    create_df_02()
    merge_df_02()
    create_df_03()
    merge_df_03()
