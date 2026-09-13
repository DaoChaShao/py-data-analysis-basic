"""
Seaborn 附带的常用数据集包括：
https://github.com/mwaskom/seaborn-data
"""

from matplotlib import font_manager

import matplotlib.pyplot as plt
import seaborn as sns


def heat_map():
    """ 热力图显示相互关系和相关性分析 """
    iris = sns.load_dataset("iris")
    print(f"鸢尾花数据集：\n{iris.head()}")
    print(f"鸢尾花数据集的形状：{iris.shape}")

    return iris


def heat_map_01():
    """ 热力图显示花冠和花萼的相关性分析 """
    iris = heat_map()
    # 去掉不相关数据列
    iris = iris.drop(['species'], axis=1)
    plt.figure(figsize=(10, 10))
    font = font_manager.FontProperties(fname="data/站酷庆科黄油体.ttf")
    # matrix 矩阵形式的热力图
    matrix = iris.corr()
    print(f"矩阵形式的热力图：\n{matrix}")
    # 绘制热力图
    sns.heatmap(
        matrix,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        annot_kws={"size": 24}
    )
    plt.title('花冠和花萼的相关性分析', fontproperties=font)
    plt.tight_layout()
    plt.show()


"""
method
pearson：皮尔逊相关系数【连续值】：衡量两个变量之间的线性相关关系，取值范围[-1,1]，1表示完全正相关，-1表示完全负相关，0表示无关。
spearman：斯皮尔曼相关系数【离散值】：衡量两个变量之间的 monotonic 相关关系，即变量随着另一个变量的变化而变化的程度。
kendall：肯德尔相关系数：衡量两个变量之间的 monotonic 相关关系，即变量随着另一个变量的变化而变化的程度。
"""


def plt_scatter_plot_tips():
    """ 散点图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    plt.figure(figsize=(5, 5))

    # 散点图
    plt.scatter(
        x="total_bill",
        y="tip",
        data=tips,
    )
    plt.tight_layout()
    plt.show()


def sns_reg_plot_tips():  # 线型回归预测参考（机器学习中的线性模型）
    """ 散点图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    plt.figure(figsize=(5, 5))

    # 散点图
    # sns.regplot(x="total_bill", y="tip", data=tips, color='orange')
    sns.regplot(x=tips.total_bill, y=tips.tip, color='blue')
    plt.tight_layout()
    plt.show()


def sns_lm_plot_tips():  # 线型回归预测参考（机器学习中的线性模型）
    """ 散点图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    # plt.figure(figsize=(5, 5))

    # 散点图
    sns.lmplot(x="total_bill", y="tip", data=tips, hue="total_bill")
    # plt.tight_layout()
    plt.show()


def sns_hist_plot_tips():
    """ 直方图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    # 直方图
    sns.histplot(
        tips.total_bill,
        bins=20,
        kde=True,
        color='blue',
        # element='step',  # 显示直方图的形状为阶梯形状
    )
    plt.tight_layout()
    plt.show()


def sns_ked_plot_tips_01():
    """ 密度图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    # 密度图
    sns.kdeplot(
        tips.total_bill,
        color='blue',
        shade=True,  # 阴影显示
        label='total_bill',
    )
    plt.tight_layout()
    plt.show()


def sns_ked_plot_tips_02():
    """ 密度图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    # 密度图
    sns.kdeplot(
        x=tips.total_bill,
        y=tips.tip,
        color='blue',
        fill=True,  # 阴影显示
        label='total_bill',
    )
    plt.tight_layout()
    plt.show()


def sns_joint_plot_tips():  # 双变量分布
    """ 联合分布图显示 tips 数据集 """
    tips = sns.load_dataset("tips")
    print(f"tips 数据集：\n{tips.head()}")
    print(f"tips 数据集的形状：{tips.shape}")

    # 联合分布图
    sns.jointplot(
        x=tips.total_bill,
        y=tips.tip,
        # color="skyblue",  # 整体颜色
        kind='scatter',  # 设置主体的图形，能够显示x，y的关系，线性回归预测
        marginal_kws=dict(bins=20, kde=True, color='orange'),  # 边缘分布图
        joint_kws=dict(alpha=0.5, color='red'),  # 点的透明度
    )
    plt.tight_layout()
    plt.show()


def sns_pair_plot_iris():  # 成对变量分布
    """ 散点图矩阵显示 iris 数据集 """
    iris = sns.load_dataset("iris")
    print(f"iris 数据集：\n{iris.head()}")
    print(f"iris 数据集的形状：{iris.shape}")

    iris = iris.drop(['species'], axis=1)
    print(f"iris 数据集去掉 species 后:：{iris}")
    print(f"iris 数据集去掉 species 后的形状：{iris.shape}")

    # 散点图矩阵
    sns.pairplot(iris)
    plt.tight_layout()
    plt.show()


# 绘制多层面板分类图
def sns_grid_plot_iris():
    tips = sns.load_dataset("tips")
    # 设置显示图标
    grid = sns.FacetGrid(
        tips,
        row="day",
        col="sex",
        aspect=2,  # 子图宽高比
    )
    # 绘制子图
    grid.map(
        plt.scatter,  # 绘制散点图，该参数一旦确定，会影响后面的参数设置，必须匹配
        "total_bill",
        "tip",
        alpha=0.5,
        color="blue",
    )
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    heat_map()
    heat_map_01()
    plt_scatter_plot_tips()
    sns_reg_plot_tips()
    sns_lm_plot_tips()
    sns_hist_plot_tips()
    sns_ked_plot_tips_01()
    sns_ked_plot_tips_02()
    sns_joint_plot_tips()
    sns_pair_plot_iris()
    sns_grid_plot_iris()
