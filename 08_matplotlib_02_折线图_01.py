import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame
from faker import Faker

from utils import lines


def df_plot_line_series():
    """ 绘制线形图，并添加数据标签 """
    index_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ]
    scores = Series(
        data=np.random.randint(0, 100, size=len(index_names)),
        index=index_names,
        name="score"
    )
    scores.plot(
        kind="line",  # 图形类型
        marker="o",  # 标记形状
        markersize=10  # 标记大小
    )
    plt.show()


def generate_df():
    data_rows = 10
    index_names = [Faker().first_name() for _ in range(data_rows)]
    cols = ["Chinese", "Mathmatics", "English", ]
    df_dict = {
        "Name": index_names,
        cols[0]: np.random.randint(0, 100, size=data_rows),
        cols[1]: np.random.randint(0, 100, size=data_rows),
        cols[2]: np.random.randint(0, 100, size=data_rows),
    }
    df = DataFrame(df_dict, index=index_names, columns=cols)
    print(f"Dataframe 数据集：\n{df}")
    print(f"Dataframe 数据集的维度：{df.shape}")

    return df


def df_plot_line_df():
    df = generate_df()
    lines()
    # 绘制线形图
    df.plot(kind="line", marker="o", markersize=3)
    plt.title("Student Scores")
    plt.legend(["Chinese", "Mathmatics", "English", ])
    plt.show()


if __name__ == "__main__":
    # df_plot_line_series()
    df_plot_line_df()
