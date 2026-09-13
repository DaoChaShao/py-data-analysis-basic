import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils import countdown


def mat_draw_circle():
    """ 通过 Matplotlib 绘制圆形 """
    x = np.linspace(-1, 1, 100)
    y = (1 - x ** 2) ** 0.5
    plt.figure(figsize=(6.0, 3.0))  # 比例设置需要优先图形绘制
    plt.plot(x, y)
    plt.show()


@countdown
def draw_sns_hist():
    """ 绘制约会总花费的直方图 """
    tips = sns.load_dataset("tips")
    # print(f"约会数据集：\n{tips}\n")
    print(f"约会数据集形状：{tips.shape}")

    # 设置画板比例
    plt.figure(figsize=(12, 6))
    # 绘制直方图
    plt.hist(
        x=tips["total_bill"],
        bins=20,  # 直方图的柱数
        rwidth=0.8,  # 直方图的宽度
        edgecolor="black",  # 边框颜色
        linewidth=1.2,  # 边框宽度
        alpha=0.5,  # 透明度
        color="g",  # 颜色
    )
    plt.show()


@countdown
def draw_sns_group_bar():
    """ 绘制不同日期的消费总额的条形图 """
    """ 绘制约会总花费的直方图 """
    tips = sns.load_dataset("tips")
    # print(f"约会数据集：\n{tips}\n")
    print(f"约会数据集形状：{tips.shape}")

    # 绘制条形图
    # 不同日期的分组
    tips_group = tips.groupby(
        "day",
        observed=True,  # 观察到的频数
        sort=True,  # 按顺序排列
    )
    # 分组后消费额求和
    y_values = tips_group["total_bill"].sum()
    print(f"不同日期的消费总额：\n{y_values}")  # 列表
    x_days = y_values.index
    print(f"不同日期：\n{x_days}")  # 列表

    # 绘制条形图
    plt.bar(
        x=np.arange(y_values.size),  # x轴坐标
        height=y_values,  # 高度
        width=0.3,
        edgecolor="black",  # 边框颜色
        linewidth=1.2,
        alpha=0.5,
        color="g",
    )
    # 设置y轴轴标签
    y_label_name = "Total Bill (unit:us$)"
    plt.ylabel(y_label_name)
    # 设置x轴轴标签
    x_label_name = "Day"
    plt.xlabel(x_label_name)
    # 设置x轴刻度标签
    x_index_list = np.arange(y_values.size)
    plt.xticks(x_index_list, x_days)
    # 设置标题
    title_name = f"Days vs Total Bill"
    plt.title(title_name)

    # 显示图形
    plt.show()


def draw_chart_in_one_figure():
    """ 将两组数据绘制在一个画板中 """
    # 设置正玄曲线数据
    x = np.linspace(-np.pi, np.pi, 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)
    # 绘制正弦曲线在一张图中
    plt.figure(figsize=(6, 3))
    plt.plot(x, sin_y)  # 绘制正弦曲线
    plt.plot(x, cos_y)  # 绘制余弦曲线
    # 显示图片
    plt.show()


def draw_chart_in_two_figures():
    """ 两两组数据分别绘制在花瓣中 """
    x = np.linspace(-np.pi, np.pi, 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)
    # 绘制正弦曲线在两张图中
    plt.figure(figsize=(6, 3))
    plt.plot(x, sin_y)  # 绘制正弦曲线
    # 显示第一张图像
    plt.show()
    # 显示第二张图像
    plt.plot(x, cos_y)  # 绘制余弦曲线
    plt.show()


if __name__ == '__main__':
    # mat_draw_circle()
    # draw_sns_hist()
    # draw_sns_group_bar()
    # draw_chart_in_one_figure()
    draw_chart_in_two_figures()
