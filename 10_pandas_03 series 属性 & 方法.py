import numpy as np
import pandas as pd
from faker import Faker


def series_shape():
    """系列的形状"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.shape


def series_size():
    """系列的大小"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.size


def series_index():
    """获取显式索引"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return f"系列：{series.index}\n索引:{series.index[0]}和{series.index[[0, 1]]}"


def series_value():
    """获取值"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return f"系列：\n{series}\n值：\n{series.values[0]}和{series.values[[0, 1]]}"


def series_search():
    """搜索值"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return (f"搜索数学的值：{series.get('数学')}\n"
            f"检查是否有数学存在：{(series.index == "数学").any()}\n"
            f"检查是否有俄语存在：{(series.index == "俄语").any()}")


def series_head():  # 是切片操作，但一般用于查看数据结构
    """获取前几行"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.head(), series.head(2)  # 不写参数则默认获取前5行


def series_tail():  # 是切片操作，但一般用于查看数据结构
    """获取后几行"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.tail(), series.tail(2)  # 不写参数则默认获取后5行


def series_nan():  # NaN : Not a Number 空值
    """处理缺失值"""
    dict = {
        "name": Faker().last_name(),
        "address": Faker().city(),
    }
    series = pd.Series(dict, index=["name", "address", "age"])
    # 判断方法有2种：
    # 1. isnull()：检查是否有缺失值，有缺失值则返回True/否则返回False （应配合any()）
    # 2. notnull()：检查是否没有缺失值，有缺失值则返回True/否则返回False （应配合all()）
    return f"{series}\n检查是否有缺失值：\n{series.isnull().any()}\n缺失细节：\n{series.isnull()}"


def series_name():
    """给系列命名"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index, name="scores")
    # series.name = "成绩"
    return series


def series_describe():
    """描述性统计"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.describe()


def series_sort_index():
    """按索引排序"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.sort_index(ascending=False)


def series_sort_values():
    """按值排序"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.sort_values(ascending=True)


def series_rfm():
    """RFM模型，最近消费时间，消费频率，消费金额和三个维度，可以用来分析客户价值和生命周期。"""
    # 假设有订单表用户id
    user_id = pd.Series(data=np.random.randint(0, 10, 100))  # 0至10的id，100个订单，其中必然有重复，重复相当于复购
    return user_id.value_counts()


def series_rename():
    """重命名索引"""
    index = ["语文", "数学", "英语", "理综"]
    series = pd.Series([80, 90, 70, 85], index=index)
    return series.rename(index={"语文": "语文成绩", "数学": "数学成绩"})


if __name__ == '__main__':
    print(series_shape())
    print(series_size())
    print(series_index())
    print(series_value())
    print(series_search())
    print(series_head())
    print(series_tail())
    print(series_nan())
    print(series_name())
    print(series_describe())
    print(series_sort_index())
    print(series_sort_values())
    print(series_rfm())
    print(series_rename())
