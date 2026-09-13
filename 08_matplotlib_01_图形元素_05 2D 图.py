from faker import Faker

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import font_manager

import seaborn as sns

import random


def hist_plot():
    """ 直方图 """
    hist_data = np.random.randn(1000)
    print(f"直方图数据集：\n{hist_data}")
    print(f"直方图数据集形状：{hist_data}")
    plt.hist(
        hist_data,
        bins=20,
        color='steelblue',
        edgecolor='black',
        alpha=0.8,
        label='Histogram',
        density=True,
    )
    sns.kdeplot(
        data=hist_data,
        color='red',
        alpha=0.5,
        label='KDE',
        linewidth=2,
    )
    plt.show()


def bar_plot_horizontal():
    """ 柱状图 """
    data_rows = 10
    index_names = [Faker().first_name() for _ in range(data_rows)]
    col_values = [random.randint(100, 500) for _ in range(data_rows)]
    plt.figure(figsize=(10, 6))
    plt.bar(
        x=index_names,
        height=col_values,
        color=Faker().hex_color(),
        align=np.random.choice(["center", "edge", ]),
        alpha=np.random.choice([0.8, 0.6, 0.4]),
    )
    plt.tight_layout()
    plt.show()


def bar_plot_vertical():
    """ 柱状图 """
    data_rows = 10
    index_names = [Faker().first_name() for _ in range(data_rows)]
    col_values = [random.randint(100, 500) for _ in range(data_rows)]
    plt.figure(figsize=(10, 6))
    plt.barh(
        y=index_names,
        width=col_values,
        color=Faker().hex_color(),
        align=np.random.choice(["center", "edge", ]),
        alpha=np.random.choice([0.8, 0.6, 0.4]),
    )
    font = font_manager.FontProperties(
        fname="站酷庆科黄油体.ttf",
        size=random.randint(16, 24),
    )
    plt.title(
        "Bar plot vertical",
        fontproperties=font,
        color=Faker().color_name(),
    )
    plt.tight_layout()
    plt.show()


def polar_plot():
    """ 极坐标图 """
    # 极坐标系的坐标范围是固定的，所以这里的角度范围是0-2pi
    plt.axes(polar=True)
    plt.show()


def polar_plot_with_data():
    """
    极坐标图：极坐标系的坐标范围是固定的，所以这里的角度范围是0-2pi
    """
    data = np.random.randint(3, 10, size=8)
    print(data)
    # 极坐标系的坐标范围是固定的，所以这里的角度范围是0-2pi
    plt.figure(figsize=(5, 5))
    plt.axes(polar=True)
    # 选角度或者选点
    angles = np.linspace(
        0, 2 * np.pi, len(data),
        endpoint=False,  # 不能包括最后一个点，否则会出现闭合的情况
    )
    print(angles)
    plt.bar(
        x=angles,
        height=data,
        color=np.random.random((len(data), 3)),
        align=np.random.choice(["center", "edge", ]),
        alpha=np.random.choice([0.8, 0.6, 0.4]),
    )
    font = font_manager.FontProperties(
        fname="data/站酷庆科黄油体.ttf",
        size=random.randint(16, 24),
    )
    plt.title(
        "Polar",
        fontproperties=font,
        color=Faker().color_name(),
    )
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # hist_plot()
    # bar_plot_horizontal()
    # bar_plot_vertical()
    # polar_plot()
    polar_plot_with_data()
