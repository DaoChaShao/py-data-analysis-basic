"""
Seaborn 附带的常用数据集包括：
https://github.com/mwaskom/seaborn-data
"""

from faker import Faker
from matplotlib import font_manager

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


def bar_chart_mlp():
    # 准备数据
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    data = [np.random.randint(1000, 10000) for _ in range(data_rows)]
    # print(data)
    plt.figure(figsize=(10, 6))
    # 绘制条形图
    plt.bar(names, data)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def bar_chart_sns():
    # 准备数据
    data_rows = 10
    names = [Faker().first_name() for _ in range(data_rows)]
    data = [np.random.randint(1000, 10000) for _ in range(data_rows)]
    # print(data)
    plt.figure(figsize=(10, 6))
    # 绘制条形图：会出现置信区间（置信区间是指根据样本数据估计出来的样本分布的上下限）
    sns.barplot(x=names, y=data)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def tips_plot_sns_01():
    """" 统计不同性别和是否抽烟的消费总额"""
    # 准备数据
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 绘制散点图
    sns.barplot(
        x="sex", y="tip",
        data=tips,
        hue="smoker",  # 增加分组信息
        hue_order=["No", "Yes"],  # 设置分组顺序
        palette="hls",  # 设置颜色
        order=["Male", "Female"],  # 设置顺序
        # errorbar=None,  # 去掉置信区间
    )
    plt.legend(title="smoker", loc="upper right")
    plt.tight_layout()
    plt.show()


def tips_plot_sns_02():
    """ 统计不同时间段的消费总额 """
    # 准备数据
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 定制颜色
    colors = {
        "Dinner": Faker().color_name(),
        "Lunch": Faker().color_name(),
    }
    # 绘制散点图
    sns.barplot(
        x="time", y="total_bill",
        data=tips,
        hue="time",
        palette=colors,  # 修改调色板：设置颜色
        estimator=np.mean,  # 修改聚合函数：计算平均值
    )
    plt.tight_layout()
    plt.show()


def tips_plot_sns_03():
    """ 根据性别和参加人数查看消费总额的分布 """
    # 准备数据
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 绘制条形图
    sns.barplot(
        x="sex", y="tip",
        data=tips,
        hue="size",
        palette="Set2",
        # errorbar=None,  # 去掉置信区间
    )
    plt.legend(title="size", loc="upper left")
    plt.tight_layout()
    plt.show()


def tips_plot_sns_04():
    """ 统计男性和女性消费者的比例 """
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    sns.countplot(
        x="sex",
        data=tips,
        hue="smoker",
        palette="Set2",
    )
    plt.legend(title="smoker", loc="upper right")
    plt.tight_layout()
    plt.show()


def titanic_sns_bar_01():
    """ 绘制泰坦尼克号乘客幸存性别比例 """
    titanic = sns.load_dataset("titanic")
    print(f"Titanic 数据集：\n{titanic}")
    print(f"Titanic 数据集形状：{titanic.shape}")
    sns.countplot(
        x="sex",
        data=titanic,
        hue="survived",
        palette="Set2",
    )
    plt.legend(title="survived", loc="upper right")
    plt.tight_layout()
    plt.show()


def tips_plot_sns_05():
    """ 统计不同性别抽烟者的分布 """
    # 准备数据
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    font_path = font_manager.FontProperties(fname="data/站酷庆科黄油体.ttf")
    # 绘制条形图
    sns.countplot(
        x="smoker",
        data=tips,
        hue="sex",
        palette="Set2",
    )
    plt.legend(title="sex", loc="upper right")
    plt.xticks(
        ticks=[0, 1],
        labels=["吸烟群体", "非吸烟群体"],
        fontproperties=font_path,
    )
    plt.tight_layout()
    plt.show()


def sns_strip_plot_01():
    """ 绘制消费总额与消费的散点图 """
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 绘制散点图
    sns.stripplot(  # strip 更适合处理离散值和连续值之间的关系，x 轴不能修改
        x="total_bill",
        y="tip",
        data=tips,
        jitter=True,  # 增加抖动
        hue="total_bill",
        palette="Set2",
    )
    plt.legend(title="total_bill", loc="upper right")
    plt.show()


def sns_strip_plot_02():
    """ 绘制消费总额与吸烟者的散点图 """
    tips = sns.load_dataset("tips")
    sns.swarmplot(  # swarm 更适合处理离散值和连续值之间的关系，x 轴可以修改
        x="smoker",
        y="total_bill",
        data=tips,
        hue="smoker",
        palette="Set2",
    )
    plt.show()


def violin_plot_01():
    """ 绘制消费总额与吸烟者的分布图 """
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 绘制 violin 图
    sns.violinplot(
        x="smoker",
        y="total_bill",
        data=tips,
        hue="smoker",
        palette="Set2",
    )
    plt.tight_layout()
    plt.show()


def violin_plot_02():
    """ 绘制消费总额与吸烟者的性别的分布图 """
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    # 绘制 violin 图
    sns.violinplot(
        x="smoker",
        y="total_bill",
        data=tips,
        hue="sex",
        palette="Set2",
        split=True,  # 显示上下分位数
    )
    plt.tight_layout()
    plt.show()


def violin_strip_plot():
    """ 绘制消费总额与吸烟者、性别的分布图 """
    tips = sns.load_dataset("tips")
    sns.violinplot(
        x="smoker",
        y="total_bill",
        data=tips,
        hue="smoker",
        palette="Set2",
    )
    sns.swarmplot(
        x="smoker",
        y="total_bill",
        data=tips,
        hue="sex",
        palette="Set1",
    )
    plt.tight_layout()
    plt.show()


def box_plot_01():
    """ 绘制消费总额与天数的箱型图 """
    tips = sns.load_dataset("tips")
    plt.figure(figsize=(10, 6))
    random_choice = random.choice(["day", "sex", "smoker", "time"])
    sns.boxplot(
        x=random_choice,
        y="total_bill",
        data=tips,
        hue=random_choice,
        palette="Set2",
        # whis=np.inf,  # 不显示离散点
    )
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    bar_chart_mlp()
    bar_chart_sns()
    tips_plot_sns_01()
    tips_plot_sns_02()
    tips_plot_sns_03()
    tips_plot_sns_04()
    titanic_sns_bar_01()
    tips_plot_sns_05()
    sns_strip_plot_01()
    sns_strip_plot_02()
    violin_plot_01()
    violin_plot_02()
    violin_strip_plot()
    box_plot_01()
