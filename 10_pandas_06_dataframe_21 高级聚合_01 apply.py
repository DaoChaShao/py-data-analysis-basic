
import numpy as np
from pandas import DataFrame
from faker import Faker
import random

from utils import countdown, lines


def generate_fake_df():
    """ 创建一个类似英雄联盟游戏人物数据的假数据集 """
    data_rows = 30
    cols = ["Name", "ID", "HP", "MP", "Attack Range", "Role"]
    hero_names = [Faker().first_name() for _ in range(data_rows)]
    ids_min = 10000
    ids_max = 20000
    hero_ids = [random.randint(ids_min, ids_max) for _ in range(data_rows)]
    hp_min = 1000
    hp_max = 10000
    hero_hp = [random.randint(hp_min, hp_max) for _ in range(data_rows)]
    mp_min = 1000
    mp_max = 10000
    hero_mp = [random.randint(mp_min, mp_max) for _ in range(data_rows)]
    # 创建攻击范围和角色的映射字典
    hero_range_and_roles_mapping = {
        "Melee": ["Warrior", "Knight"],
        "Mid-range": ["Hunter", "Rogue"],
        "Long-range": ["Mage", "Warlock"],
    }
    hero_ranges = list(hero_range_and_roles_mapping.keys())
    # print(hero_ranges)
    # 创建数据字典
    df_dict = {
        cols[0]: hero_names,
        cols[1]: hero_ids,
        cols[2]: hero_hp,
        cols[3]: hero_mp,
        cols[4]: [],
        cols[5]: [],
    }
    #  映射字典添加至数据字典
    for _ in range(data_rows):
        range_choice = random.choice(hero_ranges)
        df_dict["Attack Range"].append(range_choice)
        df_dict["Role"].append(random.choice(hero_range_and_roles_mapping[range_choice]))

    df = DataFrame(data=df_dict, columns=cols)
    print(f"仿英雄联盟游戏人物数据集：\n{df}")
    print(f"仿英雄联盟游戏人物数据集的维度：{df.shape}")

    return df


@countdown
def df_mean():
    df = generate_fake_df()
    lines()
    mean_hp = df.groupby("Role")["HP"].mean()
    mean_mp = df.groupby("Role")["MP"].mean()
    print(f"各职业的平均生命值：\n{mean_hp}")
    print(f"数据集维度：{mean_hp.shape}")
    lines()
    print(f"各职业的平均魔法值：\n{mean_mp}")
    print(f"数据集维度：{mean_mp.shape}")

    return mean_hp, mean_mp


@countdown
def df_apply():
    """ 自定义apply函数 """
    df = generate_fake_df()
    df_hp = df.groupby("Role")["HP"].apply(np.mean)  # lambda x: x.mean()
    print(f"各职业的平均生命值：\n{df_hp}")
    print(f"数据集维度：{df_hp.shape}")
    df_mp = df.groupby("Role")["MP"].apply(lambda x: x.mean())  # np.mean
    print(f"各职业的平均魔法值：\n{df_mp}")
    print(f"数据集维度：{df_mp.shape}")


if __name__ == "__main__":
    generate_fake_df()
    df_mean()
    df_apply()
