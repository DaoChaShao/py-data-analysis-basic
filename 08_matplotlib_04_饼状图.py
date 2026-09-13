from faker import Faker
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

import random


def crate_pie():
    """ 创建饼状图 """
    plt.figure(figsize=(8, 8))

    percent_male = random.randint(0, 100)
    percent_female = random.randint(0, (100 - percent_male))

    font = font_manager.FontProperties(
        fname="data/站酷庆科黄油体.ttf",
        size=random.randint(12, 28)
    )

    plt.pie(
        [percent_male, percent_female],  # 饼状图数据
        labels=["男性", "女性"],  # 标签名称
        labeldistance=1.1,  # 标签距离圆心距离
        explode=[0, 0.1],  # 突出显示的标签
        colors=["#FF7F50", "#696969"],  # 标签颜色
        autopct="%1.1f%%",  # 百分比格式
        pctdistance=0.8,  # 百分比距离圆心距离
        startangle=90,  # 起始角度
        shadow=True,  # 阴影
        radius=1.2,  # 半径
        frame=True,  # 显示边框
        wedgeprops={"edgecolor": "black", "linewidth": 1},  # 饼状图边框属性
        textprops={"fontsize": random.randint(12, 28), "fontproperties": font}
    )
    plt.title(
        "性别比例",
        fontproperties=font,
        color=Faker().color_name(),
    )
    plt.legend(
        ["男性", "女性"],
        loc=np.random.choice(["upper left", "upper right", "lower left", "lower right"]),
        prop=font,
    )
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    crate_pie()
