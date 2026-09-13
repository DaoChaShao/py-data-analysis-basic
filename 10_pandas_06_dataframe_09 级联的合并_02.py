import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines

"""
合并
合并的df一定至少存在一列内容有对应关系，否则会报错。
一般存在三种方式
1.1对1合并：当两个df的列名完全相同，且内容也完全相同，可以直接使用merge方法进行合并。
2.1对多合并：当两个df的列名完全相同，但内容不同，可以先用merge方法进行合并，然后再用concat方法进行拼接。
3.多对1合并：当两个df的列名不同，但内容完全相同，可以先用concat方法进行拼接，然后再用merge方法进行合并。
"""


def df_name_points():
    """df：姓名、分数"""
    points_rows = ["Tom", "Jerry", "Mike"]
    points_cols = ["Name", "Points"]
    points_min = 0
    points_max = 100
    df_points_dict = {
        points_cols[0]: points_rows,
        points_cols[1]: [random.randint(points_min, points_max) for _ in range(len(points_rows))],
    }
    df_points = DataFrame(df_points_dict, columns=points_cols)
    print(df_points)
    print(df_points.shape)
    return df_points


def df_name_age():
    """df：姓名、年龄"""
    age_rows = ["Tom", "Jerry", "Mike", "John"]
    age_cols = ["Name", "Age"]
    age_min = 18
    age_max = 60
    df_age_dict = {
        age_cols[0]: age_rows,
        age_cols[1]: [random.randint(age_min, age_max) for _ in range(len(age_rows))],
    }
    df_age = DataFrame(df_age_dict, columns=age_cols)
    print(df_age)
    print(df_age.shape)
    return df_age


@countdown
def merge_df_1_to_1():
    """1对1合并"""
    df_points = df_name_points()
    lines()
    df_age = df_name_age()
    lines()
    # 1对1合并
    df_merged = pd.merge(df_points, df_age)
    print(df_merged)
    print(df_merged.shape)

    lines()

    # 与concat合并的效果对比
    df_concat = pd.concat((df_points, df_age))
    print(df_concat)
    print(df_concat.shape)


def df_name_teacher_gender():
    """df：姓名、老师、性别"""
    rows = ["Tom", "Jerry", "Mike", "John", "Mary"]
    gender = ["M", "F", "M", "M", "F"]
    cols = ["Teacher", "Gender", "Name"]
    df_dict = {
        cols[0]: [random.choice(["T1", "T2", "T3"]) for _ in range(len(rows))],
        cols[1]: gender,
        cols[2]: rows,
    }
    df = DataFrame(df_dict, columns=cols)
    print(df)
    print(df.shape)
    return df


@countdown
def merge_df_1_to_n():
    """1对多合并"""
    df_points = df_name_points()
    lines()
    df_mul = df_name_teacher_gender()
    lines()
    # 1对多合并
    df_merged = pd.merge(df_points, df_mul)
    print(df_merged)
    print(df_merged.shape)


def df_name_gender_phone():
    """df：姓名、性别、手机号"""
    rows = ["Tom", "Jerry", "Mike", "John", "Mary", "Peter", "Lisa"]
    gender = ["M", "F", "M", "M", "F", "M", "F"]
    phone = [Faker().phone_number() for _ in range(len(rows))]
    cols = ["Phone Number", "Gender", "Name"]
    df_dict = {
        cols[0]: phone,
        cols[1]: gender,
        cols[2]: rows,
    }
    df = DataFrame(df_dict, columns=cols)
    print(df)
    print(df.shape)
    return df


@countdown
def merge_df_n_to_n():
    """多对多合并，默认合并列标签相同的列"""
    df_teacher = df_name_teacher_gender()
    lines()
    df_phone = df_name_gender_phone()
    lines()
    # 多对多合并
    df_merged = pd.merge(df_teacher, df_phone)
    print(df_merged)
    print(df_merged.shape)


@countdown
def merge_df_n_to_n_on():
    """多对多合并，指定合并列标签相同的列"""
    df_teacher = df_name_teacher_gender()
    lines()
    df_phone = df_name_gender_phone()
    lines()
    # 多对多合并
    df_merged = pd.merge(df_teacher, df_phone, on="Name")  # 指定列名合并
    print(df_merged)
    print(df_merged.shape)

    lines()

    # 修订由on指定列名合并后的列标签冲突
    df_suffix = pd.merge(df_teacher, df_phone, on="Name", suffixes=("_Biology", "_Self-Identification"))
    print(df_suffix)
    print(df_suffix.shape)


def df_name_age_cn():
    """df：姓名（中文）、年龄"""
    age_rows = ["Tom", "Jerry", "Mike", "John"]
    age_cols = ["姓名", "Age"]
    age_min = 18
    age_max = 60
    df_age_dict = {
        age_cols[0]: age_rows,
        age_cols[1]: [random.randint(age_min, age_max) for _ in range(len(age_rows))],
    }
    df_age = DataFrame(df_age_dict, columns=age_cols)
    print(df_age)
    print(df_age.shape)
    return df_age


@countdown
def merge_df_n_to_n_diff_col_name():
    """多对多合并，指定合并列标签不同"""
    df_en = df_name_points()
    lines()
    df_cn = df_name_age_cn()
    lines()
    # 多对多合并
    # df_merged_default = pd.merge(df_en, df_cn)  # 默认合并是无法合并的，因为无公共列标签
    # print(df_merged_default)
    # print(df_merged_default.shape)

    # 合并不同标签名
    df_merged_manual = pd.merge(df_en, df_cn, left_on="Name", right_on="姓名")
    print(df_merged_manual)
    print(df_merged_manual.shape)

    lines()

    # 删除多余列
    df_drop = df_merged_manual.drop(labels=["姓名"], axis=1)
    print(df_drop)
    print(df_drop.shape)


@countdown
def merge_how_inner():
    """合并方式：内连接/内合并"""
    df_points = df_name_points()
    lines()
    df_age = df_name_age()
    lines()
    # 内合并不写参数时，就是默认合并 = merge_df_1_to_1()
    df_merged_inner = pd.merge(df_points, df_age)
    print(f"默认合并的结果：\n{df_merged_inner}")
    print(df_merged_inner.shape)

    lines()

    df_merged_inner = pd.merge(df_points, df_age, how="inner")
    print(f"内连接的结果：\n{df_merged_inner}")
    print(df_merged_inner.shape)


@countdown
def merge_how_outer():
    """合并方式：外连接/外合并"""
    df_points = df_name_points()
    lines()
    df_age = df_name_age()
    lines()
    # 外合并时，保留所有内容，确实值由 NaN 填充
    df_merged_outer = pd.merge(df_points, df_age, how="outer")
    print(f"内连接的结果：\n{df_merged_outer}")
    print(df_merged_outer.shape)

    lines()

    # 填充 NaN 值
    points_mean = round(df_merged_outer["Points"].mean(), 2)
    df = df_merged_outer.fillna(value={"Points": points_mean})
    print(f"填充 NaN 值的结果：\n{df}")
    print(df.shape)


@countdown
def merge_how_left_and_right():
    """合并方式：左连接/左合并、右连接/右合并"""
    df_points = df_name_points()
    lines()
    df_age = df_name_age()
    lines()
    # 左连接/左合并，保留左边的全部内容，右边的匹配内容为 NaN
    df_merged_left = pd.merge(df_points, df_age, how="left")
    print(f"左连接/左合并的结果：\n{df_merged_left}")
    print(df_merged_left.shape)

    lines()

    # 右连接/右合并，保留右边的全部内容，左边的匹配内容为 NaN
    df_merged_right = pd.merge(df_points, df_age, how="right")
    print(f"右连接/右合并的结果：\n{df_merged_right}")
    print(df_merged_right.shape)


if __name__ == "__main__":
    df_name_points()
    df_name_age()
    merge_df_1_to_1()
    df_name_teacher_gender()
    merge_df_1_to_n()
    df_name_gender_phone()
    merge_df_n_to_n()
    merge_df_n_to_n_on()
    df_name_age_cn()
    merge_df_n_to_n_diff_col_name()
    merge_how_inner()
    merge_how_outer()
    merge_how_left_and_right()
