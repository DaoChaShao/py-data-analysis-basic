import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown

"""
交叉表和透视表类似
但是，交叉表更偏向于计算分组频率的特殊的透视表
"""


def generate_pivot_table():
    data_rows = 5
    random_min = 50
    random_max = 100
    semesters = ["Semester 1", "Semester 2", ]
    names = [Faker().first_name() for i in range(data_rows)]
    # 创建 MultiIndex
    rows = pd.MultiIndex.from_product([semesters, names], names=["semester", "Name"])
    cols = ["Chinese", "English", ]
    # 创建空的 DataFrame
    df = DataFrame(index=rows, columns=cols)
    for semester in semesters:
        for name in names:
            scores = [random.randint(random_min, random_max) for i in range(len(cols))]
            df.loc[(semester, name)] = scores
    print(f"原始数据集：\n{df}")
    print(f"原始数据集的维度: {df.shape}")

    return df


@countdown
def pivot_table():
    # 透视表：根据单个或多个列的值，将数据聚合到一个新的表中，作用是：
    # 1. 分析数据之间的相关性；
    # 2. 计算数据总和、均值、方差、最大值、最小值等；
    # 3. 计算不同分类的总和、均值、方差、最大值、最小值等；
    # 4. 分析数据分布的模式。
    df = generate_pivot_table()
    df_pt = pd.pivot_table(data=df, values="Chinese", index="Name", columns="semester", aggfunc="count")
    print(f"透视表:\n{df_pt}")
    print(f"透视表的维度: {df_pt.shape}")


@countdown
def crosstab():
    # 交叉表：将两个或多个分类变量的频率或计数进行比较，作用是：
    # 1. 分析两个或多个分类变量之间的关系；
    # 2. 计算不同分类组合的频率或计数；
    # 3. 分析不同分类组合之间的差异。
    df = generate_pivot_table()
    # df_ct = pd.crosstab(index=df["Name"], columns=df["Chinese"])
    df_ct = pd.crosstab(index=df.index.get_level_values("Name"), columns=df["Chinese"])
    print(f"交叉表:\n{df_ct}")
    print(f"交叉表的维度: {df_ct.shape}")


if __name__ == "__main__":
    generate_pivot_table()
    pivot_table()
    crosstab()
