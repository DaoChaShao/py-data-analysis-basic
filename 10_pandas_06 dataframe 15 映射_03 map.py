

from pandas import DataFrame
from faker import Faker
import random

from utils import lines, countdown

"""
map() 不是 df 函数，是series函数，可以对series中的每个元素进行映射操作。
"""

@countdown
def create_df_01():
    """
    创建一个包含不完全重复的重复值的 DataFrame
    """
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Name", "Chinese", "Math", "English",]
    df_dict = {
        cols[0]: names,
        cols[1]: [random.randint(0, 100) for _ in range(data_rows)],
        cols[2]: [random.randint(0, 100) for _ in range(data_rows)],
        cols[3]: [random.randint(0, 100) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def map_city():
    """ 映射城市 """
    df = create_df_01()
    lines()
    names = df["Name"].tolist()  # 姓名列表
    cities = [Faker().city() for _ in range(len(names))]  # 城市列表
    name_city_dict = {
        names[i]: cities[i] for i in range(len(names))
    }
    df["City"] = df["Name"].map(name_city_dict)
    print(f"映射后数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 获取字典映射
    random_num = random.randint(0, len(names)-1)
    get_dict_value = name_city_dict.get(names[random_num])
    print(f"通过索引 {random_num} 的 {names[random_num]} 获取字典中的城市映射：{get_dict_value}")

@countdown
def transform_score_to_gpa(score):
    """ 百分制转换成 GPA """
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0


@countdown
def map_100_to_gpa5():
    """ 映射 100 分到 GPA 5.0 """
    df = create_df_01()
    lines()
    df["Chinese"] = df["Chinese"].map(transform_score_to_gpa)  # 替换原有数值
    df["Math"] = df["Math"].map(transform_score_to_gpa)  # 替换原有数值
    df["English_GPA"] = df["English"].map(transform_score_to_gpa)  # 新增列
    print(f"映射后数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def map_lambda():
    """ 使用 lambda 表达式映射 """
    df = create_df_01()
    lines()
    df.iloc[:, 0] = df.iloc[:, 0].map(lambda x: x.upper())  # 映射姓名为大写
    df.iloc[:, 0] = df.iloc[:, 0].map(lambda x: f"Class 1 {x}")  # 映射姓名为 Class 1 开头
    print(f"映射后数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def transform_lambda():
    """ 使用 lambda 表达式转换 """
    df = create_df_01()
    lines()
    df.iloc[:, 0] = df.iloc[:, 0].transform(lambda x: x.upper())  # 转换姓名为大写
    df.iloc[:, 0] = df.iloc[:, 0].transform(lambda x: f"{x} Class 1 Stu")  # 转换姓名为 Class 1 开头
    print(f"转换后数据:\n{df}")
    print(f"数据维度：{df.shape}")


def feedback_level(scores):
    """ 反馈等级 """
    if scores >= 85:
        return "Excellent"
    elif 75 <= scores < 85:
        return "Good"
    elif 60 <= scores < 75:
        return "Pass"
    else:
        return "Fail"


@countdown
def give_feedback():
    """ 给学生反馈 """
    df = create_df_01()
    lines()
    # 重写学生分数
    random_min = 50
    random_max = 100
    df.iloc[:, 1] = [random.randint(random_min, random_max) for _ in range(len(df))]
    df.iloc[:, 2] = [random.randint(random_min, random_max) for _ in range(len(df))]
    df.iloc[:, 3] = [random.randint(random_min, random_max) for _ in range(len(df))]
    # 给学生反馈
    cols = df.columns[1:]  # 跳过 Name 列的所有列
    for col in cols:
        df[col] = df[col].map(feedback_level)
    print(f"反馈后数据:\n{df}")
    print(f"数据维度：{df.shape}")

def rate_level(scores):
    """ 反馈等级 """
    if scores >= 85:
        return "I"
    elif 75 <= scores < 85:
        return "II"
    elif 60 <= scores < 75:
        return "III"
    else:
        return "F"

@countdown
def rate_student():
    """ 给学生反馈 """
    df = create_df_01()
    lines()
    # 重写学生分数
    random_min = 50
    random_max = 100
    df.iloc[:, 1] = [random.randint(random_min, random_max) for _ in range(len(df))]
    df.iloc[:, 2] = [random.randint(random_min, random_max) for _ in range(len(df))]
    df.iloc[:, 3] = [random.randint(random_min, random_max) for _ in range(len(df))]
    # 给学生反馈
    cols = df.columns[1:]  # 跳过 Name 列
    df["Mean_all"] = df[cols].mean(axis=1).round(2)  # 计算平均分，并成为新的一列
    df["Rate"] = df["Mean_all"].map(rate_level)  # 映射到等级
    df.drop(columns=["Mean_all"], inplace=True)  # 删除原有列
    print(f"反馈后数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == "__main__":
    create_df_01()
    map_city()
    map_100_to_gpa5()
    map_lambda()
    transform_lambda()
    give_feedback()
    rate_student()