import numpy as np
from pandas import DataFrame
from faker import Faker
import random

from utils import lines, countdown


@countdown
def create_df_01():
    """
    创建一个包含不完全重复的重复值的 DataFrame
    """
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Name", "Chinese", "Math", "English", ]
    df_dict = {
        cols[0]: names,
        cols[1]: [random.randint(0, 100) for _ in range(data_rows)],
        cols[2]: [random.randint(0, 100) for _ in range(data_rows)],
        cols[3]: [random.randint(0, 100) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    # lines()

    # 添加3个重复值
    # repeat_index_01 = 3
    # repeat_index_02 = 6
    # repeat_index_03 = 9
    # df.loc[repeat_index_01] = df.loc[0].copy()  # 让第4行数据重复第1行数据的
    # df.loc[repeat_index_01, "Name"] = "Tom ***"  # 修改第4行数据的姓名，但保留与第1行一致的数据，形成不完全重复数据
    # df.loc[repeat_index_02] = df.loc[0].copy()  # 让第7行数据重复第1行数据的
    # df.loc[repeat_index_02, "Name"] = "Jerry ***"  # 修改第7行数据的姓名，但保留与第1行一致的数据，形成不完全重复数据
    # df.loc[repeat_index_03] = df.loc[0].copy()  # 让第10行数据重复第1行数据的
    # df.loc[repeat_index_03, "Name"] = "Tony ***"  # 修改第10行数据的姓名，但保留与第1行一致的数据，形成不完全重复数据
    # print(f"添加重复值后的数据:\n{df}")
    # print(f"数据维度：{df.shape}")

    return df


@countdown
def replace_value_by_regex():
    """ 使用正则表达式替换 DataFrame 中的值 """
    df = create_df_01()
    lines()

    # 使用正则表达式，将“T”开头的名字替换新姓名
    regex_name = "*** XXX ***"
    df.replace(to_replace=r"D.*", value=regex_name, regex=True, inplace=True)
    print(f"使用正则表达式替换姓名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def highest_score_replace_cheater():
    df = create_df_01()
    lines()
    # 替换100分
    random_row_min = 0
    random_row_max = 9
    random_col_min = 1
    random_col_max = 3
    position_01 = df.iloc[
        random.randint(random_row_min, random_row_max), random.randint(random_col_min, random_col_max)]
    position_02 = df.iloc[
        random.randint(random_row_min, random_row_max), random.randint(random_col_min, random_col_max)]
    position_03 = df.iloc[
        random.randint(random_row_min, random_row_max), random.randint(random_col_min, random_col_max)]
    print(position_01, position_02, position_03)
    lines()
    df.replace(to_replace=position_01, value=100, inplace=True)
    df.replace(to_replace=position_02, value=100, inplace=True)
    df.replace(to_replace=position_03, value=100, inplace=True)
    print(f"替换100分后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 标记作弊者
    df["Cheater"] = np.where(df[["Chinese", "Math", "English"]].max(axis=1) == 100, "Yes", "No")
    print(f"标记作弊者后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == '__main__':
    df = create_df_01()
    replace_value_by_regex()
    highest_score_replace_cheater()
