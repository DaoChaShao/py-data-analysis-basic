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


def sns_sin_plot():
    """ 使用 Seaborn 风格，绘制正弦曲线 """
    figure = plt.figure(figsize=(10, 6))
    font_path = font_manager.FontProperties(fname="站酷庆科黄油体.ttf")

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Seaborn 风格
    seaborn_style = random.choice(["white", "dark", "whitegrid", "darkgrid", "ticks"])
    # 用 set() 进行全局图风格设置
    sns.set(
        style=seaborn_style,
        rc={
            "font.sans-serif": [font_path.get_name()],
            "font.family": "sans-serif",
            "font.size": random.randint(12, 28),
            "axes.facecolor": Faker().color_name(),
            "axes.edgecolor": Faker().color_name(),
        },
    )
    # 用 sns.axes_style() 进行临时图风格设置
    # with sns.axes_style(seaborn_style):
    plt.plot(x, y)
    sns.despine(
        left=False,
        right=True,
        top=True,
        bottom=False,
        # trim=False,  # 设置缺角效果
    )  # 去掉边框， 且必须放在最后
    plt.show()


def color_palette():
    """ 调色板 """
    # 设置调色板
    colors = sns.color_palette(random.choice(["deep", "muted", "pastel", "bright", "dark", "colorblind"]))
    # 展示调色板
    sns.palplot(colors)
    plt.show()


def color_palette_hls():
    """ HLS 调色板 """
    colors = sns.color_palette("hls", random.randint(7, 21))
    sns.palplot(colors)
    plt.show()


def color_palette_husl():
    """ HUSL 调色板 """
    colors = sns.color_palette(
        "husl",
        random.randint(7, 21),
    )
    sns.palplot(colors)
    plt.show()


def color_palette_choose():
    """ 分类 调色板 """
    colors = sns.choose_colorbrewer_palette(
        data_type=random.choice(["diverging", "qualitative", "sequential"]),  # 需要安装并导入 ipywidgets 中的 FloatSlider
        as_cmap=False,
    )
    sns.palplot(colors)
    plt.show()


if __name__ == "__main__":
    # sns_sin_plot()
    # color_palette()
    # color_palette_hls()
    # color_palette_husl()
    color_palette_choose()
