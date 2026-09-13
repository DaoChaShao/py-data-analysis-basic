import numpy as np
import random

# 聚合：求数组的常规指标

"""
1. 平均值：np.mean(arr)
2. 中位数：np.median(arr)
3. 众数：np.mode(arr)
4. 标准差：np.std(arr)
5. 方差：np.var(arr)
6. 最大值：np.max(arr)
7. 最小值：np.min(arr)
8. 累加和：np.cumsum(arr)
9. 累乘积：np.cumprod(arr)
10. 排序：np.sort(arr)
11. 百分位数：np.percentile(arr, q)
12. 百分位数分位数：np.quantile(arr, q)
13. 协方差：np.cov(arr1, arr2)
14. 相关系数：np.corrcoef(arr1, arr2)
15. 直方图：np.histogram(arr, bins=10)
16. 累积分布函数：np.cumsum(np.histogram(arr, bins=10)[0]) / np.sum(np.histogram(arr, bins=10)[0])
17. 随机数：np.random.rand(n)
18. 正态分布随机数：np.random.normal(loc=0, scale=1, size=n)
19. 指数分布随机数：np.random.exponential(scale=1, size=n)
20. 泊松分布随机数：np.random.poisson(lam=1, size=n)
21. 均匀分布随机数：np.random.uniform(low=0, high=1, size=n)
"""

"""
一般用几个数据来描述数据水平
1. 平均值：描述数据集的中心位置 (d1 + d2 + d3 + d4 + d5 +... + dn)/n
2. 中位数：描述数据集的中间位置
3. 标准差：描述数据集的分散程度（描述数据稳定） sqrt((d1-mean)**2 + (d2-mean)**2 +... + (dn-mean)**2)/n
4. 方差：描述数据集的离散程度 ((d1-mean)**2 + (d2-mean)**2 +... + (dn-mean)**2)/n
5. 最大值：描述数据集的最高点
6. 最小值：描述数据集的最低点
"""


def np_sum():
    """数组求和"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组和: {np.sum(arr)}"


def np_mean():
    """数组求平均值"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组平均值: {np.mean(arr)}"


def np_median():
    """数组求中位数"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组中位数: {np.median(arr)}"


def np_min():
    """数组求最小值"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组最小值: {np.min(arr)}"


def np_max():
    """数组求最大值"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组最大值: {np.max(arr)}"


def np_std():
    """数组求标准差"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组标准差: {np.std(arr)}"


def np_var():
    """数组求方差"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组方差: {np.var(arr)}"


def np_argmin():
    """数组求最小值的索引"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组的最小值：{np.min(arr)}, 数组最小值的索引: {np.argmin(arr)}"


def np_argmax():
    """数组求最大值的索引"""
    arr = np.random.randint(0, 10, size=10)
    return f"数组：{arr}，数组的最大值：{np.max(arr)}, 数组最大值的索引: {np.argmax(arr)}"


def np_percentile():  # 异常值检测会使用到
    """数组求百分位数"""
    arr = np.arange(0, 11, step=1)
    return f"数组：{arr}，数组的百分位数: {np.percentile(arr, [0.25, 0.5, 0.75])}"


def np_any():
    """检测布尔数组中，是否至少存在一个ture"""
    arr = np.array([0, 0, 0, 1, 0])
    return f"数组：{arr}，数组是否有元素: {np.any(arr)}"  # 有1个0（true），返回True，全为false，返回False


def np_any_eg_01():
    bool_list = [random.randint(0, 1) for i in range(5)]
    arr = np.array(bool_list)
    return f"数组：{arr}，数组是否有元素: {np.any(arr)}"  # 有1个0（true），返回True，全为false，返回False


def np_any_eg_02():
    """找出数组中，所有大于平均值的值"""
    arr = np.random.randint(1, 11, size=10)
    # 进行广播运算: 1.为缺失的维度添加1，2.假定缺失元素已有值填充
    result = arr > np.mean(arr)
    return f"数组：{arr}\n数据平均值：{np.mean(arr)}\n布尔值列表：{result}\n大于平均值的元素: {arr[result]}"


def np_all():
    """检测布尔数组中，是否全部元素都为true"""
    arr = np.array([1, 1, 1, 1, 1])
    return f"数组：{arr}，数组是否全为元素: {np.all(arr)}"  # 全为1，返回True，有0，返回False


def np_times():
    """矩阵乘法"""
    arr_01 = np.random.randint(0, 10, size=(2, 2))  # 2x2矩阵
    arr_02 = np.random.randint(0, 10, size=(2, 2))  # 2x2矩阵
    return f"矩阵1：\n{arr_01}\n矩阵2：\n{arr_02}\n矩阵乘积: {arr_01 * arr_02}"


def np_dot():
    """（数学中的）矩阵运算"""
    arr_01 = np.random.randint(0, 10, size=(2, 2))  # 2x2矩阵
    arr_02 = np.random.randint(0, 10, size=(2, 2))  # 2x2矩阵
    return f"矩阵1：\n{arr_01}\n矩阵2：\n{arr_02}\n矩阵运算: {np.dot(arr_01, arr_02)}"


def np_sort():
    """数组排序"""
    arr = np.random.permutation(10)  # permutation() 函数，返回一个随机排列的数组，特点：每个元素都只出现一次。
    return f"数组：{arr}\n数组排序: {np.sort(arr)}"


def np_part_sort():
    """不分排序"""
    arr = np.random.permutation(20)  # permutation() 函数，返回一个随机排列的数组，特点：每个元素都只出现一次。
    return (f"数组部分排序: {np.partition(arr, 5)}\n"  # 第二个参数找的是最小的5个元素的索引，返回一个数组
            f"数组部分排序: {np.partition(arr, 5)[:5]}\n"  # 取前5个元素
            f"数组部分排序: {np.partition(arr, 5)}\n"  # 第二个参数找的是最大的5个元素的索引，返回一个数组
            f"数组部分排序: {np.partition(arr, 5)[-5:]}")  # 取后5个元素


if __name__ == "__main__":
    # np_sum()
    # np_mean()
    # np_median()
    # np_min()
    # np_max()
    # np_std()
    # np_var()
    # np_argmin()
    # np_argmax()
    # np_percentile()
    # np_any()
    # np_any_eg_01()
    # np_any_eg_02()
    # np_all()
    # np_times()
    # np_dot()
    # np_sort()
    np_part_sort()
