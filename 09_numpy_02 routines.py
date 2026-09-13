import numpy as np

from utils import countdown


# shape = (row, col)  # 几行几列的二位数组，矩阵
# shape = (m)  # m个元素的一维数组 [1, 2, 3]
# shape = (m,)  # m哥元素的一维数组

# shape = (rwo, 1)  # 几行1列的二位数组 [[1], [2], [3]]
# shape = (1, col)  # 1行几列的二位数组 [[1, 2, 3]]

# 访问一维数组和二维数组的方式不一样，索引1个还是2个

# 构造1个5行3列的二维整形数组
@countdown
def create_ny_array_01():
    ny_array = np.ones(shape=(5, 3), dtype=int)  # 5行3列的全1数组，二位数组
    print(ny_array)


# 构造1个长度为3的一维数组
@countdown
def create_ny_array_02():
    ny_array = np.ones(shape=(3,))
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构造1个5行1列的二维数组
@countdown
def create_ny_array_03():
    ny_array = np.ones(shape=(5, 1))
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构造1个1行5列的二维数组
@countdown
def create_ny_array_04():
    ny_array = np.ones(shape=(1, 5))
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构造1个2层3行4列的三位数组
@countdown
def create_ny_array_05():
    ny_array = np.zeros(shape=(2, 3, 4))
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构造1个2行3列有指定赋值的二维数组
@countdown
def create_ny_array_06():
    ny_array = np.full(shape=(2, 3), fill_value=6)
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 单位矩阵：对角线为1的矩阵 12正则项
# 构造1个3阶单位矩阵（矩阵除法）
@countdown
def create_ny_array_07():
    ny_array = np.eye(N=3)  # N 表示行数，M 表示列数；M 不写时，表示与列数一致
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


@countdown
def create_ny_array_08():
    ny_array = np.eye(N=3, M=4)  # N 表示行数，M 表示列数，M 控制形状的变化
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


@countdown
def create_ny_array_09():
    ny_array = np.eye(N=3, k=1)  # K 控制形状的变化，+1 表示向右移1位，-1 表示向左移1位
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构造1个0到10，等差为1的等差数列（相邻两个数的差相等），一维数组
@countdown
def create_ny_array_10():
    ny_array = np.linspace(start=0, stop=10, num=10)  # start 开始值，stop 结束值，num 元素个数
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


@countdown
def create_ny_array_11():
    ny_array = np.linspace(start=0, stop=10, num=10, endpoint=False)  # start 开始值，stop 结束值，num 元素个数
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


@countdown
def create_ny_array_12():
    ny_array = np.arange(start=0, stop=10, step=1)  # start 开始值，stop 结束值，step 步长
    print(f'数组的 shape 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个5行5列的随机二维数组
@countdown
def create_ny_array_13():
    ny_array = np.random.randint(low=0, high=100, size=10)  # low 最小值，high 最大值，size 元素个数（= shape）
    print(f'数组的 size 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个标准正态分布的一维数组
@countdown
def create_ny_array_14():
    ny_array = np.random.rand(100)  # 随机生成100个符合标准正态分布的随机数
    print(f'数组的随机数为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个3行5列标准正态分布的二维数组
@countdown
def create_ny_array_15():
    ny_array = np.random.rand(3, 5)  # 随机生成3行5列符合标准正态分布的随机数
    print(f'数组的随机数为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个普通正态分布的一维数组
@countdown
def create_ny_array_16():
    ny_array = np.random.normal(loc=170, scale=5)  # loc 均值，scale 标准差， 这里的170是以身高为例的身高，5是标准差
    print(f'数组的随机数为：\n {ny_array}')


# 构成1个5行5列的普通正态分布的二维数组
@countdown
def create_ny_array_17():
    ny_array = np.random.normal(loc=170, scale=5, size=(5, 5))  # loc 均值，scale 标准差， size 形状
    print(f'数组的随机数为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个0到1之间的一维数组的随机数
@countdown
def create_ny_array_18():
    ny_array = np.random.random(100)  # 随机生成100个0到1之间的随机数
    print(f'数组的随机数为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 构成1个0到1之间（左闭右开）的二位数组的随机数
@countdown
def create_ny_array_19():
    ny_array = np.random.random(size=(5, 5))  # 随机生成5行5列的0到1之间的随机数
    print(f'数组的随机数为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


# 在建模时，会用随机数引入噪声等


@countdown
def create_ny_array_20():
    """随机索引"""
    ny_array = np.random.permutation(10)  # 随机生成0到10的随机索引，用作排序
    print(f'{create_ny_array_20.__doc__} 为：\n {ny_array} \n它的类型为：{ny_array.dtype}')


@countdown
def create_ny_array_21():
    """ndim 维度"""
    ny_array = np.random.randint(0, 100, size=(5, 4, 3))  # 随机生成1个0到100的三维数组
    print(
        f'{create_ny_array_21.__doc__} 是：{ny_array.ndim}，它的 size 是：{ny_array.shape}，它的总长度是：{ny_array.size}\n'
        f'它的数组为：\n {ny_array} \n数组类型是：{type(ny_array)}，数组元素类型为：{ny_array.dtype}')


if __name__ == "__main__":
    create_ny_array_01()
    create_ny_array_02()
    create_ny_array_03()
    create_ny_array_04()
    create_ny_array_05()
    create_ny_array_06()
    create_ny_array_07()
    create_ny_array_08()
    create_ny_array_09()
    create_ny_array_10()
    create_ny_array_11()
    create_ny_array_12()
    create_ny_array_13()
    create_ny_array_14()
    create_ny_array_15()
    create_ny_array_16()
    create_ny_array_17()
    create_ny_array_18()
    create_ny_array_19()
    create_ny_array_20()
    create_ny_array_21()
