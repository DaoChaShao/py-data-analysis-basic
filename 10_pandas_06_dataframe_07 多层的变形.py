import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines

"""
多层级索引的变形
1.stack()
2.unstack()
"""


def create_dataframe():
    """创建 1 个 dataframe"""
    data_row = 5
    data_col = 3
    score_min = 0
    score_max = 100
    classes = ["class 1", "class 2", ]
    index_name = [Faker().first_name() for _ in range(data_row)]
    semesters = ["semester1", "semester2", ]
    subjects = [
        "Chinese", "Math", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    random_sub = (random.sample(subjects, k=min(data_col, len(subjects))))
    rows = pd.MultiIndex.from_product([semesters, index_name])
    df = DataFrame(index=rows, columns=random_sub)
    for semester in semesters:
        for name in index_name:
            scores = [random.randint(score_min, score_max) for _ in range(data_col)]
            df.loc[semester, name] = scores
    print(df)
    return df


@countdown
def stack_dataframe():
    """把columns变成index"""
    df = create_dataframe()
    lines()
    print(df.stack())  # 默认参数（不填）：-1 是 cols 的内层，-2 是 cols 的外层


@countdown
def unstack_dataframe():
    """把index变成columns"""
    df = create_dataframe()
    lines()
    print(df.unstack(level=-2))  # 默认参数（不填）：-1 是 rows 的内层，-2 是 rows 的外层


if __name__ == "__main__":
    create_dataframe()
    stack_dataframe()
    unstack_dataframe()
