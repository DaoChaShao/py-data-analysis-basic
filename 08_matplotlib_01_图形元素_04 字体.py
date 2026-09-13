import numpy as np

from pandas import Series

import matplotlib.pyplot as plt
from matplotlib import font_manager

from utils import lines


def create_data():
    """ 创建数据集 """
    data_len = 10
    year_start = 2000
    index_years = np.arange(year_start, year_start + data_len)
    series = Series(np.random.randint(100, 500, data_len), index=index_years)
    print(f"年份索引：{index_years}")
    lines()
    print(f"原始数据集：\n{series}")

    return series


def modify_entire_variable():
    """ 修改全局变量 """
    data = create_data()
    chart_font = font_manager.FontProperties(fname="data/站酷庆科黄油体.ttf", size=12)
    plt.plot(data)
    plt.title(
        "年收入趋势图",
        fontproperties=chart_font,
        color="red",
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # create_data()
    modify_entire_variable()
