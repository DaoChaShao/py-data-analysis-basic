import numpy as np
from faker import Faker
import random
# list 不要求数据类型一致，可以不同类型混合。
# numpy 数组要求数据类型一致且有序，并且内存空间上排列的元素是相同类型。
# 类型优先级：str > float > int

from utils import countdown


@countdown
def check_np_type_01():
    array_01 = np.array([1, 3.14, 'hello'])
    print(f'np数组为：{array_01}，它的类型为：{array_01.dtype}')  # 字符串格式，因为字符串是最后一个类型，所以会被转换为字符串格式。


@countdown
def check_np_type_02():
    array_02 = np.array([1, 3.14])
    print(f'np数组为：{array_02}，它的类型为：{array_02.dtype}')  # 只有数字，所以会被转换为浮点数格式。


@countdown
def check_np_type_03():
    array_03 = np.array([1])
    print(f'np数组为：{array_03}，它的类型为：{array_03.dtype}')  # 只有一个数字，所以会被转换为整型格式。


@countdown
def check_np_type_04():
    names = [Faker().last_name() for _ in range(5)]
    ny_array = np.array(names)
    print(f'np数组为：{ny_array}，它的类型为：{ny_array.dtype}')  # 字符串格式，因为字符串是最后一个类型，所以会被转换为字符串格式。


@countdown
def check_np_type_05():
    scores = [round(random.uniform(1, 10), 2) for _ in range(5)]  # 随机生成1到10之间的2位浮点数
    score_array = np.array(scores)
    print(f'np数组为：{score_array}，它的类型为：{score_array.dtype}')  # 因为浮点是第二个类型，所以会被转换为浮点数格式。


# 数组类型的转换
@countdown
def check_np_type_06():
    age = [random.randint(10, 99) for _ in range(5)]
    age_array = np.array(age, dtype=np.float32)
    print(f'np数组为：{age_array}，它的类型为：{age_array.dtype}')  # 整型格式，因为整型是最优先的类型。


if __name__ == '__main__':
    check_np_type_01()
    check_np_type_02()
    check_np_type_03()
    check_np_type_04()
    check_np_type_05()
    check_np_type_06()
