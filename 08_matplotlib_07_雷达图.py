import numpy as np
from pandas import DataFrame


def radar_plot():
    df_dict = {
        "Categories": ["Listening", "Reading", "Writing", "Speaking"],
        "target value": [10, 10, 10, 10],
        "current value": np.random.randint(5, 10, 4),
    }
    df = DataFrame(df_dict)
    print(f"雷达图数据集：\n{df}")
    print(f"数据集的维度：{df.shape}")

    # 设置雷达图的角度


if __name__ == "__main__":
    radar_plot()
