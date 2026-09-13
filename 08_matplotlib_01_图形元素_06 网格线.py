from faker import Faker

import numpy as np

import matplotlib.pyplot as plt


def set_grid():
    """ 设置网格线 """
    grid_style = [
        '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted',
    ]
    random_grid = np.random.choice(grid_style)
    plt.grid(True, linestyle=random_grid, alpha=0.5)
    plt.show()


def set_sub_plot_grid():
    """
    设置子画布
    1.数据会根据代码书写的位置，绘制在就近的画板中 —— 上下文原则
    2.使用 obj.axes 将数据绘制在制定的画板中 —— 面相对象原则
    """
    # 创建数据
    x = np.linspace(0, (2 * np.pi), 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)
    # 设置网格线类别
    grid_style = [
        '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted',
    ]
    line_width = ['size', 'width', 'color', 'tickdir', 'pad', 'labelsize', 'labelcolor', 'labelfontfamily', 'zorder',
                  'gridOn', 'tick1On', 'tick2On', 'label1On', 'label2On', 'length', 'direction', 'left', 'bottom',
                  'right', 'top', 'labelleft', 'labelbottom', 'labelright', 'labeltop', 'labelrotation',
                  'grid_agg_filter', 'grid_alpha', 'grid_animated', 'grid_antialiased', 'grid_clip_box', 'grid_clip_on',
                  'grid_clip_path', 'grid_color', 'grid_dash_capstyle', 'grid_dash_joinstyle', 'grid_dashes',
                  'grid_data', 'grid_drawstyle', 'grid_figure', 'grid_fillstyle', 'grid_gapcolor', 'grid_gid',
                  'grid_in_layout', 'grid_label', 'grid_linestyle', 'grid_linewidth', 'grid_marker',
                  'grid_markeredgecolor', 'grid_markeredgewidth', 'grid_markerfacecolor', 'grid_markerfacecoloralt',
                  'grid_markersize', 'grid_markevery', 'grid_mouseover', 'grid_path_effects', 'grid_picker',
                  'grid_pickradius', 'grid_rasterized', 'grid_sketch_params', 'grid_snap', 'grid_solid_capstyle',
                  'grid_solid_joinstyle', 'grid_transform', 'grid_url', 'grid_visible', 'grid_xdata', 'grid_ydata',
                  'grid_zorder', 'grid_aa', 'grid_c', 'grid_ds', 'grid_ls', 'grid_lw', 'grid_mec', 'grid_mew',
                  'grid_mfc', 'grid_mfcalt', 'grid_ms']
    colours = [Faker().color() for _ in range(len(grid_style))]
    # 设置画板
    axes_up_left = plt.subplot(
        2,  # 行数
        2,  # 列数
        1,  # 第几个子图
    )
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则
    plt.grid(
        True,
        linestyle=np.random.choice(grid_style),
        alpha=np.random.random(),
        linewidth=np.random.randint(1, 5),
        color=colours[np.random.randint(0, len(colours))],
        axis=np.random.choice(['x', 'y', 'both']),
    )  # 随机设置网格线

    axes_up_right = plt.subplot(2, 2, 2)
    axes_up_right.plot(x, sin_y)  # 面相对象原则
    plt.grid(
        True,
        linestyle=np.random.choice(grid_style),
        alpha=np.random.random(),
        linewidth=np.random.randint(1, 5),
        color=colours[np.random.randint(0, len(colours))],
        axis=np.random.choice(['x', 'y', 'both']),
    )  # 随机设置网格线

    axes_down_left = plt.subplot(2, 2, 3)
    axes_down_left.plot(x, cos_y)  # 面相对象原则
    plt.grid(
        True,
        linestyle=np.random.choice(grid_style),
        alpha=np.random.random(),
        linewidth=np.random.randint(1, 5),
        color=colours[np.random.randint(0, len(colours))],
        axis=np.random.choice(['x', 'y', 'both']),
    )  # 随机设置网格线

    axes_down_right = plt.subplot(2, 2, 4)
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则
    plt.grid(
        True,
        linestyle=np.random.choice(grid_style),
        alpha=np.random.random(),
        linewidth=np.random.randint(1, 5),
        color=colours[np.random.randint(0, len(colours))],
        axis=np.random.choice(['x', 'y', 'both']),
    )  # 随机设置网格线

    # 调整画布相对比值
    plt.figure(figsize=(10, 6))

    # 显示图像
    plt.show()


def crate_random_image_jpg():
    """
    随机生成图像
    jepg 格式的图片代表的是：三个0-255之间的随机数构成的矩阵，每个矩阵代表一个像素点
    """
    random_image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)
    plt.imshow(random_image)
    plt.show()


def crate_random_image_png():
    """
    随机生成图像
    png 格式的图片代表的是：三个0-1之间的随机数构成的矩阵，每个矩阵代表一个像素点，0代表黑色，1代表白色
    """
    random_image = np.random.random(size=(100, 100, 3))
    plt.imshow(random_image)
    plt.show()


"""
由于png是由浮点组成，所以它的精度要比jpg高，所以png更适合用于高精度的图像处理。Mac 系统 retina屏幕的出现使得png图片的分辨率提高到了原来的四倍，而jpg图片的分辨率一般是1/2到1/4。
"""

if __name__ == '__main__':
    # set_grid()
    set_sub_plot_grid()
    # crate_random_image_jpg()
    # crate_random_image_png()
