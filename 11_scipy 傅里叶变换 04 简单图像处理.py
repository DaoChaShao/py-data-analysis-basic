import matplotlib.pyplot as plt
from scipy import (ndimage,  # 图像处理
                   signal,  # 信号处理
                   datasets)  # 图像生成


def get_image():
    """ 读取图像 """
    # 使用 datasets.fact() 函数读取图像，替换了 misc.face 函数
    # image = misc.face()  # misc.face 函数已经在 SciPy v1.10.0 版本中被弃用，并且将在 v1.12.0 版本中被完全移除
    image = datasets.face()  # 但须要 pip3 install pooch  # 三维图像转二维图像，方面后续操作
    plt.imshow(image)
    plt.show()

    return image


def modify_image_two():
    image = datasets.face(gray=True)
    # 图像移动
    image_shift = ndimage.shift(image, [50, 100])  # y轴（正号）向下，x轴（正号）向右
    plt.imshow(image_shift)
    plt.show()


def modify_image_three():
    image = datasets.face()
    # 图像移动
    image_shift = ndimage.shift(
        image,
        [50, -100, 0],
        mode="mirror",  # 填充黑色区域
    )  # y轴（正号）向下，x轴（负号）向左，z轴
    plt.imshow(image_shift)
    plt.show()

    # 图像上下颠倒
    image_up_down = image_shift[::-1]  # 这里是切片操作：行，列，维：维颠倒
    # image_up_down = np.flipud(image_shift)
    plt.imshow(image_up_down)
    plt.show()

    # 图像左右颠倒
    image_left_right = image_shift[:, ::-1]  # 这里是切片操作：行，列，维：列颠倒
    plt.imshow(image_left_right)
    plt.show()

    # 图像剪裁
    image_cropped = image_shift[300:600, 380:620]  # 这里是切片操作：行，列，维：剪裁
    plt.imshow(image_cropped)
    plt.show()

    # 图像旋转
    image_rotated = ndimage.rotate(image_shift, 45)  # 旋转角度
    plt.imshow(image_rotated)
    plt.show()

    # 图像缩放
    image_zoomed = ndimage.zoom(image_shift, [0.5, 0.5, 1])
    plt.imshow(image_zoomed)
    plt.show()

    # 足够的小的话，可以出现马赛克效果
    image_zoomed = ndimage.zoom(image_shift, [0.075, 0.075, 1])
    plt.imshow(image_zoomed)
    plt.show()


def image_filter_ndimage():
    image = datasets.face()
    # 图像模糊
    image_blur = ndimage.gaussian_filter(image, sigma=10)  # 高斯模糊
    plt.imshow(image_blur)
    plt.show()


def image_gaussian_std():  # 高斯分布 = 正态分布
    """ 高斯滤波 """
    image_path = "data/scipy_matrix.png"
    # 读取图像
    image = plt.imread(image_path)
    plt.imshow(image, cmap="gray")
    plt.show()

    # 使用相邻值填充
    # 高斯降噪：标准差
    ndimage.gaussian_filter(image, sigma=3)
    plt.imshow(image, cmap="gray")
    plt.show()


def image_gaussian_median():  # 高斯分布 = 正态分布
    """ 高斯滤波 """
    image_path = "data/scipy_matrix.png"
    # 读取图像
    image = plt.imread(image_path)
    plt.imshow(image, cmap="gray")
    plt.show()
    # 高斯降噪：中位数
    ndimage.median_filter(image, size=5)
    plt.imshow(image, cmap="gray")
    plt.show()


def image_signal():
    """ 信号滤波 """
    image_path = "data/scipy_matrix.png"
    # 读取图像
    image = plt.imread(image_path)
    signal.wiener(image, mysize=5)
    plt.imshow(image, cmap="gray")
    plt.show()


if __name__ == '__main__':
    get_image()
    modify_image_two()
    modify_image_three()
    image_filter_ndimage()
    image_gaussian_std()
    image_gaussian_median()
    image_signal()
