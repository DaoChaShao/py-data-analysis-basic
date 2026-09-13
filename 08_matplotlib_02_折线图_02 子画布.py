from mimesis import Food, Finance
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt

"""
变量分析：
单变量分析：Series
多变量分析：DataFrame
"""


def line_series_line():
    """ 单变量分析：Series """
    data_rows = 10
    data_names = [Food().dish() for _ in range(data_rows)]
    data_values = [Finance().price_in_btc(100, 500) for _ in range(data_rows)]
    # print(data_names)
    # print(data_values)

    # 创建 Series 数据
    series = Series(data_values, index=data_names)
    print(f"Series 数据集：\n{series}")
    print(f"Series 数据集的形状：{series.shape}")

    # 绘制折线图
    plt.plot(
        series.index,  # x 轴数据
        series.values,  # y 轴数据
        marker='o',
        markersize=5,
    )
    # 调整数据参数
    plt.xticks(rotation=60, ha="center")  # 旋转 x 轴标签
    plt.xlabel("Food Name")  # 设置 x 轴标签名
    plt.ylabel("Price")  # 设置 y 轴标签名
    plt.title("Food & Price")  # 设置标题
    plt.tight_layout()  # 自动调整子图间距
    # 显示图像
    plt.show()


def draw_lines():
    """ 绘制多个图形在一块画板中 """
    x = np.linspace(0, (2 * np.pi), 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)

    # 方法一
    # plt.plot(x, sin_y)
    # plt.plot(x, cos_y)
    # 方法二
    plt.plot(x, sin_y, x, cos_y, )
    plt.tight_layout()
    plt.show()


def set_sub_plot():
    """
    设置子画布
    1.数据会根据代码书写的位置，绘制在就近的画板中 —— 上下文原则
    2.使用 obj.axes 将数据绘制在制定的画板中 —— 面相对象原则
    """
    # 创建数据
    x = np.linspace(0, (2 * np.pi), 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)
    # 设置画板
    axes_up_left = plt.subplot(
        2,  # 行数
        2,  # 列数
        1,  # 第几个子图
    )
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则

    axes_up_right = plt.subplot(2, 2, 2)
    axes_up_right.plot(x, sin_y)  # 面相对象原则

    axes_down_left = plt.subplot(2, 2, 3)
    axes_down_left.plot(x, cos_y)  # 面相对象原则

    axes_down_right = plt.subplot(2, 2, 4)
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则

    # 调整画布相对比值
    plt.figure(figsize=(10, 6))

    # 显示图像
    plt.show()


if __name__ == '__main__':
    # line_series_line()
    # draw_lines()
    set_sub_plot()
