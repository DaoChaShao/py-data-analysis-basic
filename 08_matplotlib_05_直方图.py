import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
from faker import Faker


def generate_fake_data():
    """ Generate fake data for testing. """
    data_rows = 10
    index_names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["HP"]
    df_dict = {
        "Name": index_names,
        "HP": np.random.randint(10, 50, data_rows),
    }
    df = DataFrame(df_dict, index=index_names, columns=cols)
    print(f"original data:\n{df}")
    print(f"original shape:\n{df.shape}")

    return df


def df_plot_hist():
    """ Plot histogram of dataframe. """
    df = generate_fake_data()
    df.plot(
        kind="hist",
        bins=5,  # 设置直方图的柱子数量
        alpha=0.5,  # 设置透明度
        figsize=(10, 6),
    )
    plt.show()


def df_plot_hist_randn():
    # 创建正态分布数据
    data = Series(np.random.randn(3000))
    # 绘制直方图
    data.plot(kind="hist", bins=60, alpha=0.5, density=True)
    # scipy 库对于绘制核密度估计（KDE）图是必要的，需要安装 scipy 库
    # 绘制核密度估计图
    data.plot(kind="kde", color="red")
    plt.show()


if __name__ == "__main__":
    # df_plot_hist()
    df_plot_hist_randn()
