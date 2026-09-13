

import pandas as pd
from pandas import DataFrame
from faker import Faker
import random

from utils import lines, countdown

@countdown
def create_df_01():
    """
    创建一个包含不完全重复的重复值的 DataFrame
    """
    random_min = 50
    random_max = 100
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Name", "Chinese", "Math", "English",]
    df_dict = {
        cols[0]: names,
        cols[1]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[2]: [random.randint(random_min, random_max) for _ in range(data_rows)],
        cols[3]: [random.randint(random_min, random_max) for _ in range(data_rows)],
    }
    df = DataFrame(df_dict, columns=cols)
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def rename_cols():
    """ 重命名 DataFrame 的列名 """
    df = create_df_01()
    lines()
    current_cols = df.columns
    rename_dict = {
        current_cols[0]: "姓名",
        current_cols[1]: "语文",
        current_cols[2]: "数学",
        current_cols[3]: "英语",
    }
    df = df.rename(columns=rename_dict)
    # 设置列宽选项
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"重命名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def rename_rows():
    """ 重命名 DataFrame 的行名 """
    df = create_df_01()
    lines()
    # 先去掉原索引，将姓名作为索引
    df.set_index("Name", inplace=True)
    # 获取当前姓名索引
    current_rows = df.index
    # 生成新的姓名索引
    new_rows = [Faker(locale="zh_CN").name() for _ in range(len(df))]
    # 重命名行名
    rename_row_dict = {
        current_rows[i]: new_rows[i] for i in range(len(current_rows))
    }
    df = df.rename(index=rename_row_dict)
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"重命名行名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 替换列索引
    cols = df.columns
    rename_col_dict = {
        cols[0]: "语文",
        cols[1]: "数学",
        cols[2]: "英语",
    }
    df = df.rename(columns=rename_col_dict)
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"替换列索引后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def rename_mapper():
    """ 使用 mapper 重命名 DataFrame 的列名和行名 """
    # 接收 df
    df = create_df_01()
    lines()
    # 去掉原索引，使用姓名作为索引
    df.set_index("Name", inplace=True)
    # 使用级联扩大数据规模
    df = pd.concat((df, df), axis=1, keys=["Semester 1", "Semester 2"])
    print(f"级联扩大数据规模后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 重命名行名
    # 设置 mapper 字典，重命名列名
    current_names = df.index.tolist()
    new_names = [Faker(locale="zh_CN").name() for _ in range(len(df))]
    mapper_names_dict = {
        current_names[i]: new_names[i] for i in range(len(current_names))
    }
    mapper_dict = {
        "Chinese": "语文",
        "Math": "数学",
        "English": "英语",
        "Semester 1": "第一学期",
        "Semester 2": "第二学期",
    }
    # 将名字字典添加到 mapper 字典中
    mapper_dict.update(mapper_names_dict)
    # 使用 mapper 重命名行名
    df.rename(mapper=mapper_dict, axis=0, inplace=True)
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"使用 mapper 重命名【行名】后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 使用 mapper 重命名列名外层
    df.rename(mapper=mapper_dict, axis=1, inplace=True, level=-2)
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"使用 mapper 重命名【列名 外层】后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 使用 mapper 重命名列名内层
    df.rename(mapper=mapper_dict, axis=1, inplace=True, level=-1)
    pd.set_option('display.unicode.east_asian_width', True)  # 设置中文显示列宽选项
    print(f"使用 mapper 重命名【列名 内层】后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == "__main__":
    create_df_01()
    rename_cols()
    rename_rows()
    rename_mapper()