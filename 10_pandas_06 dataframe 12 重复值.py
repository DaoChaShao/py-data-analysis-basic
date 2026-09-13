from pandas import DataFrame
from faker import Faker
import random

from utils import lines, countdown

"""
原始数据清洗的基本步骤：
1.了解数据：head(), info(), describe()
2.空值处理
3.异常值处理
4.重复值处理
5.数据类型转换
6.数据规范化
--------------------------
7.数据集成
8.数据可视化
9.数据导出
"""

@countdown
def create_df_01():
    """
    创建一个包含完全重复的重复值的 DataFrame
    """
    data_rows = 5
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

    lines()

    # 添加3个完全的重复值
    df.loc[data_rows + 0] = df.loc[0].copy()  # 复制第一行数据
    df.loc[data_rows + 1] = df.loc[1].copy()  # 复制第二行数据
    df.loc[data_rows + 2] = df.loc[2].copy()  # 复制第三行数据
    print(f"添加重复值后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

    return df


@countdown
def conduct_repeated_value_01():
    """处理重复值"""
    df = create_df_01()
    lines()
    # 按照标签名查找重复值
    bool_list = df.duplicated()  # keep='first'默认保留第一次出现的重复值, keep='last'保留最后一次出现的重复值, 默认为 last
    print(f"重复值索引：\n{bool_list}")
    print(f"重复值数量：{bool_list.sum()}")

    lines()

    # 查看重复值
    df_dup = df[bool_list]
    print(f"重复值有 {df_dup.shape[0]} 个，具体如下:\n{df_dup}")
    print(f"数据维度：{df_dup.shape}")

    lines()

    # 删除重复值
    df.drop_duplicates(keep="last", inplace=True)  # 保留后出现的重复值
    print(f"删除重复值后的数据:\n{df}")
    print(f"数据维度：{df.shape}")

@countdown
def create_df_02():
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
def conduct_repeated_value_02():
    """处理重复值"""
    df = create_df_02()
    lines()
    # 按照标签名查找重复值
    bool_list = df.duplicated()  # 按照Name查询，是查看不出不完全重复数据的
    print(f"重复值索引：\n{bool_list}")
    print(f"重复值数量：{bool_list.sum()}")

    lines()

    # 按照数据内容一致性查询
    bool_sub_list = df.duplicated(subset=["Chinese", "Math", "English"], keep=False)  # keep=False表示返回重复数据的索引
    print(f"重复值索引：\n{bool_sub_list}")
    print(f"重复值数量：{bool_sub_list.sum()}")

    lines()

    # 查看过滤后的重复值
    df_dup = df[bool_sub_list]
    print(f"过滤后的重复值有 {df_dup.shape[0]} 个，具体如下:\n{df_dup}")
    print(f"数据维度：{df_dup.shape}")

    lines()

    # 删除重复值
    df.drop_duplicates(subset=["Chinese", "Math", "English"], inplace=True)  # 按照数据内容一致性删除重复值
    print(f"删除重复值后的数据:\n{df}")
    print(f"数据维度：{df.shape}")


if __name__ == "__main__":
    create_df_01()
    conduct_repeated_value_01()
    create_df_02()
    conduct_repeated_value_02()
