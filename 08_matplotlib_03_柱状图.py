import matplotlib as mpl  # 控制外观（包括字体）
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
from faker import Faker


def df_plot_bar_series():
    """ 绘制线形图，并添加数据标签 """
    data_rows = 10
    index_names = [Faker().first_name() for _ in range(data_rows)]
    scores = Series(
        data=np.random.randint(0, 100, size=len(index_names)),
        index=index_names,
        name="score"
    )
    scores.plot(
        kind="bar",  # 图形类型
    )
    plt.show()


def generate_bar_data():
    data_rows = 10
    index_name = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Semester 1", "Semester 2", "Semester 3", ]
    df_dict = {
        "Name": index_name,
        cols[0]: np.random.randint(0, 100, size=len(index_name)),
        cols[1]: np.random.randint(0, 100, size=len(index_name)),
        cols[2]: np.random.randint(0, 100, size=len(index_name)),
    }
    df = pd.DataFrame(df_dict, index=index_name, columns=cols)
    print(f"柱状图数据集:\n{df}")
    print(f"柱状图数据集维度:\n{df.shape}")

    return df


def df_plot_bar_df():
    df = generate_bar_data()
    df.plot(
        kind="bar",  # 图形类型：竖向柱状图
    )
    plt.show()


def df_plot_bar_df_stack():
    df = generate_bar_data()
    df.stack().unstack(level=-2).plot(
        kind="bar",  # 图形类型： 竖向柱状图
    )

    plt.show()


def df_plot_bar_df_customised():
    df = generate_bar_data()
    # 重写数据姓名
    df.index = [Faker(locale="zh_CN").name() for _ in range(len(df))]
    print(f"重写数据姓名:\n{df}")
    # 设置中文显示
    mpl.rcParams["font.sans-serif"] = ["Arial Unicode MS"]  # 用来正常显示中文标签
    mpl.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号
    # 绘制柱状图
    df.plot(
        kind="barh",  # 图形类型：横向柱状图
        figsize=(5, 10)  # 第一个值表示宽度，第二个值表示高度
    )
    plt.show()


if __name__ == "__main__":
    # df_plot_bar_series()
    # df_plot_bar_df()
    # df_plot_bar_df_stack()
    df_plot_bar_df_customised()
