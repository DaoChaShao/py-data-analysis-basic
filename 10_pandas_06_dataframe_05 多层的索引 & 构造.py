import numpy as np
import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines


def create_dataframe():
    random_min = 0
    random_max = 100
    df_row = 3
    df_col = 6
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    random_subjects = (random.sample(subjects, k=min(df_col, len(subjects))))
    index_name = [Faker().name() for _ in range(df_row)]
    # data_dict = {
    #     random_subjects[0]: [random.randint(random_min, random_max) for _ in range(df_row)],
    #     random_subjects[1]: [random.randint(random_min, random_max) for _ in range(df_row)],
    #     random_subjects[2]: [random.randint(random_min, random_max) for _ in range(df_row)],
    #     random_subjects[3]: [random.randint(random_min, random_max) for _ in range(df_row)],
    #     random_subjects[4]: [random.randint(random_min, random_max) for _ in range(df_row)],
    #     random_subjects[5]: [random.randint(random_min, random_max) for _ in range(df_row)],
    # }
    data_dict = {
        subject: [random.randint(random_min, random_max) for _ in range(df_row)]
        for subject in random_subjects
    }
    df = DataFrame(data_dict, index=index_name, columns=random_subjects)
    print(df)
    return df


@countdown
def add_nan_and_fill_auto():
    df = create_dataframe()
    lines()
    # 添加 NaN 值
    random_nan_row = random.randint(0, df.shape[0] - 1)
    random_nan_col = random.randint(0, df.shape[1] - 1)
    df.iloc[random_nan_row, random_nan_col] = np.nan
    print(df)
    lines()
    # 自动填充 NaN 值
    # df = df.apply(lambda row: row.ffill(), axis=1)  # 行的向前填充，用Nan的前一个值填充
    df = df.apply(lambda row: row.bfill(), axis=1)  # 行的向后填充，用Nan的后一个值填充
    # df = df.apply(lambda col: col.ffill(), axis=0)  # 列的向前填充，用Nan的上一个值填充
    # df = df.apply(lambda col: col.bfill(), axis=0)  # 列的向后填充，用Nan的下一个值填充
    print(df)


@countdown
def add_nan_and_fill_manual():
    df = create_dataframe()
    lines()
    # 添加 NaN 值
    df.iloc[0, 0] = np.nan
    print(df)
    lines()
    # 用右下角的数值，手动填充 NaN 值
    fill_value = df.iloc[2, 5]
    print(fill_value)  # 右下角数
    lines()
    # 手动填充 NaN 值
    df.fillna(fill_value, inplace=True)
    print(df)


@countdown
def create_hierarchical_dataframe_multi_col_01():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    columns = pd.MultiIndex.from_product([semesters, random_subjects])
    # 创建一个空的DataFrame
    df = pd.DataFrame(index=index_name, columns=columns)
    # 填充数据
    for semester in semesters:
        for subject in random_subjects:
            # 生成随机分数数据
            scores = [random.randint(score_min, score_max) for _ in range(data_row)]
            # 将分数填充到DataFrame中的对应位置
            df[(semester, subject)] = scores
    print(df)


@countdown
def create_hierarchical_dataframe_multi_col_02():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    columns = pd.MultiIndex.from_product([semesters, random_subjects])
    random_data = np.random.randint(score_min, score_max, size=(data_row, (data_col * 2)))
    # 创建一个空的DataFrame
    df = pd.DataFrame(data=random_data, index=index_name, columns=columns)
    print(df)


@countdown
def create_hierarchical_dataframe_multi_row_01():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    rows = pd.MultiIndex.from_product([semesters, index_name])
    # 创建一个空的DataFrame
    df = DataFrame(index=rows, columns=random_subjects)
    # 填充数据
    for semester in semesters:
        for name in index_name:
            # 生成随机分数数据
            scores = [random.randint(score_min, score_max) for _ in range(data_col)]
            # 将分数填充到DataFrame中的对应位置
            df.loc[(semester, name)] = scores
    print(df)


@countdown
def create_hierarchical_dataframe_multi_row_02():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    rows = pd.MultiIndex.from_product([semesters, index_name])
    random_data = np.random.randint(score_min, score_max, size=((data_row * 2), data_col))
    # 创建一个空的DataFrame
    df = pd.DataFrame(data=random_data, index=rows, columns=random_subjects)
    print(df)


@countdown
def create_hierarchical_dataframe_multi_col_and_row_01():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    classes = ["class 1", "class 2", ]
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    rows = pd.MultiIndex.from_product([classes, index_name])
    cols = pd.MultiIndex.from_product([semesters, random_subjects])
    # 创建一个空的DataFrame
    df = pd.DataFrame(index=rows, columns=cols)
    # 填充数据
    for semester in semesters:
        for name in index_name:
            # 生成随机分数数据
            scores = [random.randint(score_min, score_max) for _ in range(data_col)]
            # 将分数填充到DataFrame中的对应位置
            df.loc[(slice(None), name), semester] = scores
    print(df)


@countdown
def create_hierarchical_dataframe_multi_col_and_row_02():
    data_row = 10
    data_col = 3
    score_min = 0
    score_max = 100
    classes = ["class 1", "class 2", ]
    index_name = [Faker().name() for _ in range(data_row)]
    subjects = [
        "Chinese", "Mathmatics", "English",
        "Physics", "Chemistry", "Biology",
        "History", "Geography", "Politics",
    ]
    semesters = ["Semester 1", "Semester 2"]
    random_subjects = (random.sample(subjects, k=min(data_col, len(subjects))))
    rows = pd.MultiIndex.from_product([classes, index_name])
    cols = pd.MultiIndex.from_product([semesters, random_subjects])
    random_data = np.random.randint(score_min, score_max, size=((data_row * 2), (data_col * 2)))
    # 创建一个空的DataFrame
    df = pd.DataFrame(data=random_data, index=rows, columns=cols)
    print(df)


if __name__ == "__main__":
    create_dataframe()
    add_nan_and_fill_auto()
    add_nan_and_fill_manual()
    create_hierarchical_dataframe_multi_col_01()
    create_hierarchical_dataframe_multi_col_02()
    create_hierarchical_dataframe_multi_row_01()
    create_hierarchical_dataframe_multi_row_02()
    create_hierarchical_dataframe_multi_col_and_row_01()
    create_hierarchical_dataframe_multi_col_and_row_02()
