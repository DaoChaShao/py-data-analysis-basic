import matplotlib.pyplot as plt
from matplotlib import font_manager


def give_notes():
    figure = plt.figure(
        figsize=(10, 5),
        dpi=300,
        facecolor="lightgray",
    )
    # 设置字体
    font = font_manager.FontProperties(fname="data/站酷庆科黄油体.ttf")
    # 设置画板
    axis_01 = plt.subplot(1, 2, 1, facecolor="white", )
    axis_02 = plt.subplot(1, 2, 2, facecolor="black", )
    # 设置标题
    figure.suptitle("图形元素 注释 例子", fontsize=16, fontweight="bold", fontproperties=font)
    # 设置注释
    axis_01.text(x=0.5, y=0.5, s="我是图1的注释", fontproperties=font, fontsize=12, color="blue")
    figure.text(x=0.75, y=0.95, s="我是备注，x和y参数都是相对位置", fontproperties=font, fontsize=12, color="red")
    # 图像显示
    plt.show()


if __name__ == '__main__':
    give_notes()
