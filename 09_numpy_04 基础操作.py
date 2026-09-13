import numpy as np
# 使用reshape函数将数组变形

from utils import countdown, lines


@countdown
def reshape_array():
    """将数组元素个数一致的数组变形"""
    ny_arr_01_dim = np.random.randint(0, 10, size=(20,))
    print(f"一维数组：\n {ny_arr_01_dim}\n数组维度：{ny_arr_01_dim.ndim}，数组元素个数：{ny_arr_01_dim.size}")
    lines()
    ny_arr_02_dim = ny_arr_01_dim.reshape((4, 5))
    print(f"一维数组变形后的数组：\n {ny_arr_02_dim}\n数组维度：{ny_arr_02_dim.ndim}，数组元素个数：{ny_arr_02_dim.size}")


@countdown
def display_array():
    """np.concatenate() 级联"""
    ny_arr_02_dim_01 = np.random.randint(0, 10, size=(3, 3))
    ny_arr_02_dim_02 = np.random.randint(10, 20, size=(3, 3))
    print("常规数组显示：")
    print(ny_arr_02_dim_01)
    print(ny_arr_02_dim_02)
    lines()
    print(f"{display_array.__doc__}：")
    lines()
    print(np.concatenate((ny_arr_02_dim_01, ny_arr_02_dim_02), axis=0))  # 0表示按列级联
    lines()
    print(f"{display_array.__doc__}：")
    lines()
    print(np.concatenate((ny_arr_02_dim_01, ny_arr_02_dim_02), axis=1))  # 1表示按行级联


@countdown
def ny_hstack_array():
    """np.hstack() 堆叠"""
    ny_arr_02_dim_01 = np.random.randint(0, 10, size=(3, 3))
    ny_arr_02_dim_02 = np.random.randint(10, 20, size=(3, 3))
    # 等价于np.concatenate((ny_arr_02_dim_01, ny_arr_02_dim_02), axis=1)
    print(f"{ny_hstack_array.__doc__}：")
    lines()
    print(np.hstack((ny_arr_02_dim_01, ny_arr_02_dim_02)))


@countdown
def ny_vstack_array():
    """np.vstack() 堆叠"""
    ny_arr_02_dim_01 = np.random.randint(0, 10, size=(3, 3))
    ny_arr_02_dim_02 = np.random.randint(10, 20, size=(3, 3))
    # 等价于np.concatenate((ny_arr_02_dim_01, ny_arr_02_dim_02), axis=0)
    print(f"{ny_vstack_array.__doc__}")
    lines()
    print(np.vstack((ny_arr_02_dim_01, ny_arr_02_dim_02)))


@countdown
def split_array_01():  # 只能分割偶数个元素
    """np.split_array() 分割"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(6, 6))
    print(f"原始二维数组：\n {ny_arr_02_dim}")
    lines()
    print(f"分割后的数组：\n {np.split(ny_arr_02_dim, indices_or_sections=2)}")  # 不写axis默认按行分割
    lines()
    part_01, part_02 = np.split(ny_arr_02_dim, indices_or_sections=2, axis=0)  # 0 横向分割，1 纵向分割
    print(f"分割后的数组：\npart_01\n {part_01}\npart_02\n {part_02}")


@countdown
def split_array_02():
    """np.split_array() 分割"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(3, 7))
    print(f"原始二维数组：\n {ny_arr_02_dim}")
    lines()
    print(f"分割后的数组：\n {np.split(ny_arr_02_dim, indices_or_sections=(2, 5), axis=1)}")  # 按列分割


@countdown
def hsplit_array():
    """np.hsplit() 横向分割"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(3, 7))
    print(f"原始二维数组：\n {ny_arr_02_dim}")
    lines()
    print(f"分割后的数组：\n {np.hsplit(ny_arr_02_dim, indices_or_sections=(2, 5))}")  # 按列分割


@countdown
def vsplit_array():
    """np.vsplit() 纵向分割"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(3, 7))
    print(f"原始二维数组：\n {ny_arr_02_dim}")
    lines()
    print(f"分割后的数组：\n {np.vsplit(ny_arr_02_dim, indices_or_sections=(1, 1))}")  # 按行分割


@countdown
def copy_array():
    """np.copy_array() 复制"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(3, 5))
    print(f"原始二维数组：\n {ny_arr_02_dim}")
    lines()
    ny_arr_02_dim_copy = np.copy(ny_arr_02_dim)
    print(f"复制后的数组：\n {ny_arr_02_dim_copy}")


@countdown
def copy_array_ui():
    """np.copy_array() 复制"""
    ny_arr_02_dim = np.random.randint(10, 99, size=(3, 5))
    ny_arr_02_dim_copy = np.copy(ny_arr_02_dim)
    return f"复制后的数组：\n {ny_arr_02_dim_copy}"


if __name__ == "__main__":
    # reshape_array()
    # display_array()
    # ny_hstack_array()
    # ny_vstack_array()
    # split_array_01()
    # split_array_02()
    # hsplit_array()
    # vsplit_array()
    # copy_array()
    copy_array_ui()
