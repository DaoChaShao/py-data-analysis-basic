import numpy as np
from pandas import Series
from faker import Faker
import random

"""
新建一个包含“文综”的Series，s2，与包含“理综”的s1进行多种运算
"""


def series_basic_info():
    series_index_01 = ["语文", "数学", "英语", "理综", ]
    series_index_02 = ["语文", "数学", "英语", "文综", ]
    s_science = Series(data=np.random.randint(0, 150, size=4), index=series_index_01, name="理科")
    s_arts = Series(data=np.random.randint(0, 150, size=4), index=series_index_02, name="文科")
    print(s_science)
    print(s_arts)
    return s_science, s_arts


def calculation_01():
    """NaN和任何值运算，均为NaN"""
    s_science, s_arts = series_basic_info()
    return s_science + s_arts


def calculation_02():
    """在运算时处理NaN，使用fill_value()方法"""
    s_science, s_arts = series_basic_info()
    result = s_science.add(s_arts, fill_value=0)
    return result


def calculation_03():
    """在运算前处理NaN，使用字典式的扩展方法"""
    s_science, s_arts = series_basic_info()
    s_science["文综"] = 0
    s_arts["理综"] = 0
    result = s_science + s_arts
    return result


"""
随机生成2组学生成绩，一组为python，一组Java，并进行运算
1.计算每个学生成绩的平均分
2.找出python中的未及格
3.找出java中的未及格
4.给一个学生的python + 10分
5.计算各学科的平均成绩
"""


def basic_info():
    name_index = [Faker().last_name() for _ in range(4)]
    series_python = Series(data=np.random.randint(0, 100, size=4), index=name_index, name="python")
    series_java = Series(data=np.random.randint(0, 100, size=4), index=name_index, name="java")
    print(series_python)
    print(series_java)
    return series_python, series_java


def average_score():
    """计算每个学生成绩的平均分"""
    series_python, series_java = basic_info()
    average_grade = round((series_python + series_java) / 2, 2)
    return average_grade


def find_failing_students():
    """找出python和java中的未及格学生的姓名"""
    series_python, series_java = basic_info()
    failing_python = series_python.loc[series_python < 60]
    print(failing_python)
    failing_python_name = failing_python.index.tolist()  # tolist() 是一个 NumPy 的方法，用于将数组或者矩阵转换为 Python 列表。
    failing_java = series_java.loc[series_java < 60]
    print(failing_java)
    failing_java_name = failing_java.index.tolist()
    return failing_python_name, failing_java_name


def add_score():
    """随机给一个学生的python和java + 一个随机分"""
    series_python, series_java = basic_info()
    # 获取第二个学生的姓名（由于2个数组用的是同一个index，所以可以选择任何一个数列获取姓名）
    random_choice = random.randint(0, 4)
    student_name = series_python.index[random_choice]
    random_score = random.randint(0, 10)
    # 给第二个学生的python + 10分
    series_python[student_name] += random_score
    # 给第二个学生的java + 10分
    series_java[student_name] += random_score
    print(
        f"第 {random_choice + 1} 位的学生 {student_name} 的python增加了 {random_score} 分后为 {series_python[student_name]} ")
    print(
        f"第 {random_choice + 1} 位的学生 {student_name} 的java增加了 {random_score} 分后为 {series_java[student_name]} ")
    return series_python, series_java


def average_grade_by_subject():
    """计算各学科的平均成绩"""
    series_python, series_java = basic_info()
    average_python_mean = round(series_python.mean(), 2)
    average_python_values_mean = series_python.values.mean()  # 另一种计算平均分的方法
    print(f"python平均分为 {average_python_mean} , 另一种计算平均分的方法为 {average_python_values_mean} ")
    average_java_mean = round(series_java.mean(), 2)
    average_java_values_mean = series_java.values.mean()
    print(f"java平均分为 {average_java_mean} , 另一种计算平均分的方法为 {average_java_values_mean} ")
    return average_python_values_mean, average_java_values_mean


if __name__ == "__main__":
    print(calculation_01())
    print(calculation_02())
    print(calculation_03())
    print(basic_info())
    print(average_score())
    print(find_failing_students())
    print(add_score())
    print(average_grade_by_subject())
