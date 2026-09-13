import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad  # 用于积分
from scipy import io  # 用于读取 mat 格式文件（二进制文件）

from utils import countdown


def draw_half_circle():
    # 不规则图像的函数
    l_func = lambda x: (1 - x ** 2) ** 0.5  # 根据坐标轴上的圆的勾股定理反推
    x = np.linspace(-1, 1, 100)
    y = l_func(x)
    # 绘制半圆
    plt.figure(figsize=(6, 6))  # 画半圆：（6， 3）
    plt.plot(x, y, )
    plt.plot(x, -y)
    # 图像显示
    plt.show()


def calc_area():
    """ 计算半圆（不规则图形）面积 """
    f = lambda x: (1 - x ** 2) ** 0.5  # 调用函数
    # 利用积分求半圆面积，半径：1， 圆心：(0, 0)
    area, error = quad(f, -1, 1)  # area：（半圆）面积， error：误差
    print(f"半径为 1 的半圆面积：{area:.4f}")  # 保留4位小数
    print(f"半径为 1 的正圆面积：{(area * 2):.4f}")  # 半圆面积乘以2，得到正圆面积


def mat_file_save():
    # 图像路径
    image_path = "data/scipy_matrix.png"
    # 读取图像数据
    image = plt.imread(image_path)  # 如果不需要matplotlib查看，则可以省略此步
    # 保存图像（二进制）
    io.savemat("data/scipy_matrix.mat", {"image_01": image})


def mat_file_load():
    image = "data/scipy_matrix.mat"
    # 读取图像（二进制）
    mat_data = io.loadmat("data/scipy_matrix.mat")
    mat_image = mat_data["image_01"]
    print(f"二进制文件数据：\n{mat_data}")
    print(f"图像数据：\n{mat_image}")

    # 查看图片
    plt.imshow(mat_image)
    plt.axis("off")  # 关闭坐标轴
    plt.show()


if __name__ == '__main__':
    draw_half_circle()
    calc_area()
    mat_file_save()
    mat_file_load()
