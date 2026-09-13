import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines


def generate_hierarchical_df():
    data_row = 5
    data_col = 2
    score_min = 0
    score_max = 100
    # 设置多级行
    classes = ["class1", "class2", ]
    index_name = [Faker().name() for i in range(data_row)]
    rows = pd.MultiIndex.from_product([classes, index_name])
    # 设置多级列
    semesters = ["semester1", "semester2", ]
    subjects = [
        "Chinese", "Math", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics"
    ]
    random_subjects = random.sample(subjects, k=min(data_col, len(subjects)))
    cols = pd.MultiIndex.from_product([semesters, random_subjects])
    # 创建空dataframe
    df = DataFrame(index=rows, columns=cols)
    # 填充数据
    for semester in semesters:
        for name in index_name:
            scores = [random.randint(score_min, score_max) for i in range(data_col)]
            df.loc[(slice(None), name), semester] = scores
    print(df)
    return df


@countdown
def cut_hierarchical_df():
    df = generate_hierarchical_df()
    lines()
    print(f"数据维度：{df.shape}")
    lines()
    # 访问 semester 1 的第一列数据。用元组表达索引逻辑
    print(f"semester 1 的第一列数据 如下：\n{df.iloc[:, 0]}")
    lines()
    # 访问 semester 2 的两列数据
    print(f"semester 2 的两列数据 如下：\n{df.iloc[:, 2:4]}")  # 左闭右开：2，,3
    lines()
    # 访问 class 1 的第 2 个学生的所有列数据
    count_start = 2
    print(f"class1 的第 {count_start} 个学生 {df.index[(1)][1]} 的所有列数据 如下：\n{df.iloc[0, :]}")
    lines()
    # 访问 class 1 的第 2 个至 第 4 个学生的有列数据
    count_end = 4
    print(f"class1 的第 {count_start} 个至 第 {count_end} 个学生的所有列数据 如下：\n{df.iloc[2:4, :]}")  # 左闭右开
    lines()
    # 访问 class 2 的第 2 个学生的第 2 列数据
    print(f"class2 的第 {count_start} 个学生 {df.index[6][1]} 的第 2 列数据 如下：\n{df.iloc[6, 1]}")
    lines()
    # 重新赋值
    df.iloc[6, 1] = 200
    print(f"重新赋值后的数据如下：\n{df}")


if __name__ == "__main__":
    generate_hierarchical_df()
    cut_hierarchical_df()
