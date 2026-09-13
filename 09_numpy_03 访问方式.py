import numpy as np

from utils import countdown, lines


@countdown
def func_list_cut():
    """列表的访问方式"""
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(data_list)
    lines()
    print(data_list[0])
    lines()
    print(data_list[0][0])
    lines()
    print(*data_list)
    lines()
    print(*data_list[0])


@countdown
def func_ny_cut_01():
    """数组的访问方式"""
    data_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"数组为：\n {data_arr}\n数组元素类型：{data_arr.dtype}")
    lines()
    print(data_arr[0])
    lines()
    print(f"与列表相同的访问方式：{data_arr[0][0]}")  # 与列表一样的访问方式
    lines()
    print(f"数组特有的访问方式：{data_arr[0, 0]}")  # 与列表一样的访问方式，对应维度的索引值
    lines()
    print(*data_arr)
    lines()
    print(*data_arr[0])


@countdown
def func_ny_cut_02():
    """数组的高级访问方式"""
    data_arr_01 = np.array([1, 2, 3, 4, 5])
    data_arr_02 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    bool_list = [True, False, True, False, True]
    print(data_arr_01)
    lines()
    print(data_arr_02)
    lines()

    # 高级访问方法
    # 使用列表作为索引，访问内部数据
    print(data_arr_01[[0, 1]])  # 访问数组的第0、1个元素
    lines()
    print(data_arr_01[[0, 1, 0, 1]])  # 访问数组的第0、1、0、1个元素
    lines()

    # 访问bool数组
    print(data_arr_01[bool_list])  # 访问数组的bool列表，返回True对应的元素
    lines()

    # e.g. 读取列表中 >3 的元素
    print(data_arr_01[data_arr_01 > 3])  # 访问数组的bool列表，返回True对应的元素，返回列表[False, False, False, True, True]


@countdown
def func_ny_cut_03():
    """三维数组的访问方式"""
    data_arr = np.random.randint(0, 10, size=(5, 4, 3))  # 随机生成5x4x3的数组
    print(f"数组为：\n {data_arr}\n数组元素类型：{data_arr.dtype}")
    lines()
    print(data_arr[0])
    lines()
    print(data_arr[0, 1])
    lines()
    print(data_arr[0, 1, 2])


@countdown
def func_ny_cut_04():
    """数组的切片"""  # 切片都是左闭右开
    data_arr_1_dim = np.random.randint(0, 10, size=(10,))  # 随机生成10个1x1的数组
    data_arr_2_dim = np.random.randint(0, 10, size=(5, 4))  # 随机生成4x3的数组
    data_arr_3_dim = np.random.randint(0, 10, size=(3, 4, 5))  # 随机生成5x4x3的数组
    print(f"一维数组为：\n {data_arr_1_dim}\n数组元素类型：{data_arr_1_dim.dtype}")
    lines()
    print(f"二维数组为：\n {data_arr_2_dim}\n数组元素类型：{data_arr_2_dim.dtype}")
    lines()
    print(f"三维数组为：\n {data_arr_3_dim}\n数组元素类型：{data_arr_3_dim.dtype}")
    lines()

    # 一维数组切片
    print(f"切片前：{data_arr_1_dim}，切片后：{data_arr_1_dim[0:3]}")
    lines()

    # 二维数组切片
    # 行切片
    print(f"切片前：\n {data_arr_2_dim}\n切出前2行：\n {data_arr_2_dim[0:2]}")  # 切出前两行
    lines()
    print(f"切片前：\n {data_arr_2_dim}\n切出前2行中的第2个数：\n {data_arr_2_dim[0:2, 1]}")  # 切出前两行中的第2个数
    lines()
    # 列切片
    print(f"切片前：\n {data_arr_2_dim}\n切出前2列：\n {data_arr_2_dim[:, 0:2]}")  # 切出前两列
    lines()
    # 三维数组切片
    print(f"切片前：\n {data_arr_3_dim}\n切出前2个：\n {data_arr_3_dim[0:2, :, :]}")  # 切出前两个
    lines()
    print(f"切片前：\n {data_arr_3_dim}\n切出前2行：\n {data_arr_3_dim[:, 0:2, :]}")  # 切出前两行
    lines()
    print(f"切片前：\n {data_arr_3_dim}\n切出前2行中的第2个数：\n {data_arr_3_dim[:, 0:2, 1]}")  # 切出前两行中的第2个数
    lines()
    print(f"切片前：\n {data_arr_3_dim}\n切出前2列：\n {data_arr_3_dim[:, :, 0:2]}")  # 切出前两列


@countdown
def func_ny_cut_05():
    """数组的数据反转"""
    data_arr_1_dim = np.random.randint(0, 10, size=(10,))  # 随机生成10个1x1的数组
    data_arr_2_dim = np.random.randint(0, 10, size=(5, 4))  # 随机生成4x3的数组
    data_arr_3_dim = np.random.randint(0, 10, size=(3, 4, 5))  # 随机生成5x4x3的数组
    print(f"一维数组为\n {data_arr_1_dim}\n数组元素类型：{data_arr_1_dim.dtype}")
    lines()
    print(f"一维数组颠【整体】倒后为\n {data_arr_1_dim[::-1]}")
    lines()
    print(f"二维数组为\n {data_arr_2_dim}\n数组元素类型：{data_arr_2_dim.dtype}")
    lines()
    print(f"二维数组【行】颠倒后为\n {data_arr_2_dim[::-1]}")
    lines()
    print(f"二维数【列】颠倒后为\n {data_arr_2_dim[:, ::-1]}")
    lines()
    print(f"三维数组为\n {data_arr_3_dim}\n数组元素类型：{data_arr_3_dim.dtype}")
    lines()
    print(f"三维数组【个】颠倒后为\n {data_arr_3_dim[::-1]}")
    lines()
    print(f"三维数组【行】颠倒后为\n {data_arr_3_dim[:, ::-1, :]}")
    lines()
    print(f"三维数组【列】颠倒后为\n {data_arr_3_dim[:, :, ::-1]}")


if __name__ == '__main__':
    # func_list_cut()
    # func_ny_cut_01()
    # func_ny_cut_02()
    # func_ny_cut_03()
    # func_ny_cut_04()
    func_ny_cut_05()
