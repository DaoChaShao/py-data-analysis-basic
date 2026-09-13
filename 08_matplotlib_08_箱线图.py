import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def box_plot():
    """ 箱线图 """
    data = np.random.randn(100)
    plt.boxplot(data)
    plt.show()


"""
箱线图：
用来表示离散值和连续值变量的分布情况。

箱线图由五个部分组成：

- 箱体：由上下两个边界和中位数组成，表示数据的分布范围。
- 中间线：表示数据的中位数。
- 顶部线：表示上四分位数。
- 底部线：表示下四分位数。
- 异常点：表示离群值，即数据点与上下四分位数的距离过大。
"""


def tips_box_plot():
    """ 绘制tips数据集的箱线图 """
    # 加载数据
    tips = sns.load_dataset('tips')
    # 绘制箱线图：day和tips
    # 提取数值型变量和分类变量
    days = tips['day'].unique()
    tip_data = [tips[tips['day'] == day]['tip'] for day in days]
    plt.boxplot(tip_data, tick_labels=days)
    plt.show()


if __name__ == '__main__':
    # box_plot()
    tips_box_plot()
