import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack  # 用于傅里叶变换

from utils import countdown, lines

"""
numpy 是一个运算包，解决的是：数组运算
scipy 是一个运算包，解决的是：科学运算
"""

# 1. 傅里叶变换
# 傅里叶变换是指将时域信号转换到频域信号的过程。
# 频域信号的表示方法是指将信号的频率成分表示出来，频率成分的大小反映了信号的强度。
# 傅里叶变换的目的是将时域信号分解为频域信号，从而方便对信号进行分析、处理和识别。

# 时域空间 和 频域空间

"""
1、时域空间向频域空间转换 scipy.fftpack.fft2()
2、频域空间向时域空间转换 scipy.fftpack.ifft2()
"""


def scipy_read_image():
    # 照片读取
    image = plt.imread('data/scipy_matrix.png')
    print(f"图片读取后的结果：\n{image}")
    print(f"图片读取后的形状：{image.shape}")  # (4842, 3228, 3) 3个通道的RGB图像
    """
    二维图像称为灰度图像，每一个像素点表达的是一个灰度，不是颜色。
    三维图像称为彩色图像， 每一个像素点表达的是一个颜色，有红绿蓝三个通道，RGB来描述颜色。
    """
    # 照片展示
    # 将照片数据添加至图像展示模块中
    plt.imshow(
        image,  # 图像数据
        # cmap='gray',  # 图像色彩映射，调色板设置为灰色
    )
    # 图像展示
    plt.show()

    return image


@countdown
def scipy_reduce_image_noise():
    """ 使用 scipy.fftpack.fft2() 降低图像噪声 """
    # 获取图像数据
    image = plt.imread('data/scipy_matrix.png')
    # 将时域信号转换到频域信号
    image_t_to_w = fftpack.fft2(image)
    print(f"时域信号转换到频域信号后的结果：\n{image_t_to_w}")
    print(f"时域信号转换到频域信号后的形状：{image_t_to_w.shape}")
    lines()

    # 设置波的筛选阈
    print(f"波的最大值：{np.abs(image_t_to_w).max()}")  # 最大值
    print(f"波的最小值：{np.abs(image_t_to_w).min()}")  # 最小值
    print(f"波的平均值：{np.abs(image_t_to_w).mean()}")  # 平均值
    lines()
    threshold = 1000 * np.abs(image_t_to_w).mean()  # 设定阈值，超过该值的波都认为是噪声
    threshold_bool_list = np.abs(image_t_to_w) > threshold  # 噪声bool列表
    # 把噪声部分归零
    image_t_to_w[threshold_bool_list] = 0
    print(f"滤波后的频域信号：\n{image_t_to_w}")
    print(f"滤波后的频域信号形状：{image_t_to_w.shape}")
    lines()

    # 把频域转换回时域
    image_w_to_t = fftpack.ifft2(image_t_to_w)

    # 把时域中的虚数部分去掉
    image_w_to_t = np.real(image_t_to_w)
    print(f"虚数部分去掉后的频域信号：\n{image_w_to_t}")
    print(f"虚数部分去掉后的频域信号形状：{image_w_to_t.shape}")
    lines()

    # 调整图像数据的范围以便显示
    image_w_to_t = np.clip(image_w_to_t, 0, 1)

    # 图像展示
    plt.imshow(image_w_to_t)
    plt.show()


if __name__ == '__main__':
    scipy_read_image()
    scipy_reduce_image_noise()
