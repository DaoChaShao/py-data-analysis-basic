import numpy as np
import matplotlib.pyplot as plt

"""
图形的默认值是由数据决定的
"""


def set_sin_line():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

    return x, y


def modify_sin_line():
    x, y = set_sin_line()
    plt.plot(x, y)
    # 设置画布
    canvas = plt.subplot(111)
    # 设置坐标轴范围
    # 方法一：画板设置
    # canvas.set_xlim(-1, 8)
    # canvas.set_ylim(-2, 2)
    # 方法二：直接设置
    plt.xlim(-1, 8)
    plt.ylim(-2, 2)
    # 图像显示
    plt.show()


def plot_customised_set():
    """
    设置子画布
    1.数据会根据代码书写的位置，绘制在就近的画板中 —— 上下文原则
    2.使用 obj.axes 将数据绘制在制定的画板中 —— 面相对象原则
    """
    # 创建数据
    x = np.linspace(0, (2 * np.pi), 100)
    sin_y = np.sin(x)
    cos_y = np.cos(x)
    # 设置画板
    plt.figure(figsize=(10, 6))  # 设置画布大小
    # 设置画板
    canvas_up_left = plt.subplot(
        2,  # 行数
        2,  # 列数
        1,  # 第几个子图
    )
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则
    canvas_up_left.set_xlabel(
        'Name',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )
    canvas_up_left.set_ylabel(
        'Value',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )

    canvas_up_right = plt.subplot(2, 2, 2)
    canvas_up_right.plot(x, sin_y)  # 面相对象原则
    canvas_up_right.set_xlabel(
        'Name',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )
    canvas_up_right.set_ylabel(
        'Value',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度

    )

    canvas_down_left = plt.subplot(2, 2, 3)
    canvas_down_left.plot(x, cos_y)  # 面相对象原则
    canvas_down_left.set_xlabel(
        'Name',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )
    canvas_down_left.set_ylabel(
        'Value',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )

    canvas_down_right = plt.subplot(2, 2, 4)
    plt.plot(x, sin_y)  # 上下文原则
    plt.plot(x, cos_y)  # 上下文原则
    canvas_down_right.set_xlabel(
        'Name',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )
    canvas_down_right.set_ylabel(
        'Value',
        color=np.random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'pink']),  # 随机颜色
        fontsize=np.random.randint(10, 30),  # 随机字体大小
        rotation=np.random.randint(0, 90),  # 随机旋转角度
    )

    # 设置子画布间距
    plt.subplots_adjust(bottom=0.3, left=0.3)  # 调整子画布间距，比例调整

    # 调整画布相对比值
    plt.tight_layout()

    # 显示图像
    # plt.show()

    # 保存图像
    plt.savefig(
        'data/sin_and_cos.png',
        dpi=300,  # 图像分辨率
        transparent=False,  # 背景透明
        bbox_inches='tight',  # 去除白边
        facecolor='black',  # 背景颜色
    )


if __name__ == '__main__':
    # set_sin_line()
    # modify_sin_line()
    plot_customised_set()
