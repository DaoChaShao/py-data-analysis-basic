import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns  # 用于美化绘图

from utils import lines

"""
描述两个数据的关系
"""


def scatter_plot_two():
    """ 两组数据之间的关系 """
    # 准备数据
    data_x = np.random.randn(1000)
    data_y = np.random.randn(1000)
    df_data = {
        "x": data_x,
        "y": data_y
    }
    df = DataFrame(df_data)
    df.plot(kind="scatter", x="x", y="y", alpha=0.5)
    plt.show()


def scatter_plot_three():
    """ 三组数据之间的两两关系 """
    # 准备数据
    data_x = np.random.randn(1000)
    data_y = np.random.randn(1000)
    data_z = np.random.randn(1000)
    df_data = {
        "x": data_x,
        "y": data_y,
        "z": data_z
    }
    df = DataFrame(df_data)
    pd.plotting.scatter_matrix(df)
    plt.show()


def scatter_seaborn_tips():
    """ 两组数据之间的关系 """
    # 准备数据
    tips = sns.load_dataset("tips")
    print(f"约会/小费 数据集：\n{tips}")

    lines()

    # 绘制散点图
    tips.plot(kind="scatter", x="total_bill", y="tip", alpha=0.5)
    plt.show()


def scatter_plotting():
    # 准备数据
    tips = sns.load_dataset("tips")
    print(f"约会/小费 数据集：\n{tips}")

    lines()

    # 绘制散点图
    pd.plotting.scatter_matrix(tips)
    plt.show()


if __name__ == '__main__':
    # scatter_plot_two()
    # scatter_plot_three()
    # scatter_seaborn_tips()
    scatter_plotting()
