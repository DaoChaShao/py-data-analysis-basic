import matplotlib.pyplot as plt
import numpy as np

from utils import countdown, lines

"""
将灰度图像进行傅里叶变换，可以有两种方式：
1.直接对三维进行聚合操作
2.使用矩阵乘法，完成权重划分

使三个数变成一个灰度值（三个数变成一个数
"""


@countdown
def scipy_image_min():
    """ 直接对三维进行聚合操作 """
    # 读取图像数据
    image = plt.imread("data/scipy.jpg")
    # print(f"图像数据：\n{image}")
    print(f"图像数据的维度：{image.shape}")
    lines()
    # 对图像数据（RGB）直接进行聚合
    image_mean = image.min(axis=2)
    # print(f"图像数据被直接聚合后：\n{image_mean}")
    print(f"图像数据被直接聚合后的维度：{image_mean.shape}")

    # 显示图片
    plt.imshow(image_mean, cmap="gray")
    plt.show()


@countdown
def scipy_image_mean():
    """ 直接对三维进行聚合操作 """
    # 读取图像数据
    image = plt.imread("data/scipy.jpg")
    # print(f"图像数据：\n{image}")
    print(f"图像数据的维度：{image.shape}")
    lines()
    # 对图像数据（RGB）直接进行聚合
    image_mean = image.mean(axis=2)
    # print(f"图像数据被直接聚合后：\n{image_mean}")
    print(f"图像数据被直接聚合后的维度：{image_mean.shape}")

    # 显示图片
    plt.imshow(image_mean, cmap="gray")
    plt.show()


@countdown
def scipy_image_max():
    """ 直接对三维进行聚合操作 """
    # 读取图像数据
    image = plt.imread("data/scipy.jpg")
    # print(f"图像数据：\n{image}")
    print(f"图像数据的维度：{image.shape}")
    lines()
    # 对图像数据（RGB）直接进行聚合
    image_mean = image.max(axis=2)
    # print(f"图像数据被直接聚合后：\n{image_mean}")
    print(f"图像数据被直接聚合后的维度：{image_mean.shape}")

    # 显示图片
    plt.imshow(image_mean, cmap="gray")
    plt.show()


@countdown
def scipy_image_matrix():
    """ 使用矩阵乘法，完成权重划分 """
    # 读取图像数据
    image = plt.imread("data/scipy.jpg")
    # print(f"图像数据：\n{image}")
    print(f"图像数据的维度：{image.shape}")
    lines()
    # 对图像数据（RGB）进行权重划分
    weight = np.array([0.2989, 0.5870, 0.1140])
    image_matrix = np.dot(image, weight)  # .doc 矩阵乘法
    # print(f"图像数据被权重划分后：\n{image_matrix}")
    print(f"图像数据被权重划分后的维度：{image_matrix.shape}")

    # 显示图片
    plt.imshow(image_matrix, cmap="gray")
    plt.show()

    # 保存图像数据在图像文件中
    plt.imsave("data/scipy_matrix.png", image_matrix, cmap="gray")


if __name__ == "__main__":
    scipy_image_min()
    scipy_image_mean()
    scipy_image_max()
    scipy_image_matrix()
