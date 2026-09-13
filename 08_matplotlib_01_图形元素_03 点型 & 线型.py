import numpy as np

from pandas import Series
import matplotlib.pyplot as plt

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


def create_chart():
    """ 创建图表 """
    data = create_data()
    plt.figure(figsize=(10, 6))
    axes = plt.subplot(
        111,
        # facecolor=np.random.choice(['red', 'blue', 'green', 'yellow', 'orange', ]),
    )
    plt.plot(
        data,
        color=np.random.choice(['red', 'blue', 'green', 'yellow', 'orange', ]),
        linewidth=np.random.choice([1, 2, 3, 4, 5]),
        alpha=np.random.choice([0.3, 0.5, 0.8]),
        marker=np.random.choice(["^", "<", ">", "*", "|", "_"]),
        markersize=np.random.choice([3, 6, 9]),
        markerfacecolor=np.random.choice(['red', 'blue', 'green', 'yellow', 'orange', ]),
        markeredgecolor=np.random.choice(['red', 'blue', 'green', 'yellow', 'orange', ]),
        linestyle=np.random.choice(['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']),
    )
    plt.legend(["Salary"], loc="upper left")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # create_data()
    create_chart()
