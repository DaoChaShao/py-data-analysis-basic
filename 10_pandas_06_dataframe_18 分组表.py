
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
def group_by_attack_range():
    """ 按照攻击范围分组 """
    df = generate_fake_df()
    lines()
    df_group = df.groupby(df.iloc[:, 4]).groups  # 按照攻击范围分组
    print(f"按照攻击范围分组，可分为：{len(df_group)} 组")
    lines()
    for group_name, group_members in df_group.items():
        print(f"组 {group_name:^15} ，成员包括：{group_members}")

    lines()

    # 聚合：mean()、sum()、count()、min()、max()
    df_mean = df.groupby(df.iloc[:, 4])[["HP", "MP"]].mean()
    print(f"按照攻击范围分组后，各组的平均值：\n{df_mean}")
    print(f"按照攻击范围分组后，各组的平均值维度：{df_mean.shape}")

    lines()

    # 根据需要聚合
    # 聚合字典
    agg_dict = {
        "HP": "mean",
        "MP": "sum",
        "Attack Range": "count",
    }
    df_agg = df.groupby(df.iloc[:, 4]).agg(agg_dict)
    print(f"按照攻击范围分组后，各组的聚合值：\n{df_agg}")
    print(f"按照攻击范围分组后，各组的聚合值维度：{df_agg.shape}")


@countdown
def df_group_multi():
    df = generate_fake_df()
    lines()
    # 按照攻击范围和角色分组
    df_group = df.groupby([df.iloc[:, 4], df.iloc[:, 5]]).groups
    print(f"按照攻击范围和角色分组，可分为：{len(df_group)} 组")
    print(df_group)
    lines()
    for dict_keys, group_values in df_group.items():
        hero_range, hero_role = dict_keys
        print(f"组 {hero_range:^15}丨{hero_role:^10}  ，成员包括：{group_values}")

    lines()

    # 聚合：mean()、sum()、count()、min()、max()
    agg_dict = {
        "HP": "mean",
        "MP": "sum",
        "Attack Range": "count",
    }
    df_agg = df.groupby([df.iloc[:, 4], df.iloc[:, 5]]).agg(agg_dict)
    print(f"按照攻击范围和角色分组后，各组的聚合值：\n{df_agg}")
    print(f"按照攻击范围和角色分组后，各组的聚合值维度：{df_agg.shape}")

    lines()

    # 行外侧标签转化为列标签
    df_agg_unstacked = df_agg.unstack(level=-2, fill_value=0)
    print(f"行外侧标签转化为列标签：\n{df_agg_unstacked}")
    print(f"行外侧标签转化为列标签维度：{df_agg_unstacked.shape}")


if __name__ == "__main__":
    generate_fake_df()
    group_by_attack_range()
    df_group_multi()
