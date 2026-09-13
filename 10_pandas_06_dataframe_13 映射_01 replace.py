

from pandas import DataFrame
from faker import Faker
import random

from utils import lines, countdown

"""
映射：是指将一个变量的值映射到另一个变量的不同取值上。（替换）
replace 属于 fillna 的高级版本
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

    lines()

    # 添加3个重复值
    repeat_index_01 = 3
    repeat_index_02 = 6
    df.loc[repeat_index_01] = df.loc[0].copy()  # 让第4行数据重复第1行数据的
    df.loc[repeat_index_01, "Name"] = "*** Tom ***"  # 修改第4行数据的姓名，但保留与第1行一致的数据，形成不完全重复数据
    df.loc[repeat_index_02] = df.loc[0].copy()  # 让第7行数据重复第1行数据的
    df.loc[repeat_index_02, "Name"] = "*** Jerry ***"  # 修改第7行数据的姓名，但保留与第1行一致的数据，形成不完全重复数据
    print(f"添加重复值后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def replace_value():
    """
    使用 replace 替换 DataFrame 中的值
    """
    df = create_df_01()
    lines()
    # 获取数据中想要被替换的姓名
    current_name = df.iloc[3, 0]
    new_name = "--- TOM ---"
    # 定义映射关系
    df.replace(to_replace=current_name, value=new_name, inplace=True)
    print(f"替换姓名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def replace_value_list_method():
    """ 使用 list 方法批量替换 DataFrame 中的值 """
    df = create_df_01()
    lines()
    current_names = [df.iloc[3, 0], df.iloc[6, 0]]
    new_names = ["--- TOM ---", "--- JERRY ---"]
    df.replace(to_replace=current_names, value=new_names, inplace=True)
    print(f"使用 list 方法替换姓名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def replace_value_dict_method():
    """ 使用 dict 方法替换 DataFrame 中的值 """
    df = create_df_01()
    lines()
    map_dict = {
        df.iloc[3, 0]: "--- TOM ---",
        df.iloc[6, 0]: "--- JERRY ---",
    }
    df.replace(to_replace=map_dict, inplace=True)
    print(f"使用 dict 方法替换姓名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


@countdown
def create_df_02():
    df = create_df_01()
    lines()
    # 给数据添加新列
    df["Old Name"] = df["Name"]
    print(f"原始数据:\n{df}")
    print(f"数据维度：{df.shape}")

    lines()

    # 用 dict 方法替换 Name 列中的值
    dict_key = "Name"
    dict_value = df.iloc[3, 0]
    new_name = "--- TOM ---"
    df.replace(to_replace={dict_key: dict_value}, value=new_name, inplace=True)
    print(f"使用 dict 方法替换姓名后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == "__main__":
    create_df_01()
    replace_value()
    replace_value_list_method()
    replace_value_dict_method()
    create_df_02()
