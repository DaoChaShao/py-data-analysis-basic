
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from faker import Faker
import random

from utils import countdown, lines


def numpy_array():
    # arr = np.ones(shape=(3, 5))
    arr = np.random.randint(0, 100, size=(3, 5))
    print(arr)
    return arr


@countdown
def array_calculation():
    arr = numpy_array()
    lines()
    arr_mean = arr.mean()
    print(f"数组的均值：{arr_mean}")
    lines()
    arr_std = arr.std()
    print(f"数组的标准差：{arr_std}")
    lines()
    arr_sum = arr.sum()
    print(f"数组的和：{arr_sum}")


@countdown
def cal_arr_sum_row():
    """所有行上的列的数字求和"""
    arr = numpy_array()
    lines()
    cal_result = arr.sum(axis=1)  # 0表示按行求和，1表示按列求和
    print(f"按行求和的结果：{cal_result}")


@countdown
def cal_arr_sum_col():
    """所有行上的列的数字求和"""
    arr = numpy_array()
    lines()
    cal_result = arr.sum(axis=0)  # 0表示按行求和，1表示按列求和
    print(f"按行求和的结果：{cal_result}")


def data_frame():
    fake_data_len = 10
    random_min = 50
    random_max = 100
    index_name = [Faker().name() for _ in range(fake_data_len)]
    fake_dict = {
        "Chinese": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Mathmatics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "English": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Physics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Chemistry": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Biology": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
    }
    df = DataFrame(fake_dict, index=index_name)
    print(df)
    return df


@countdown
def cal_df():
    """计算dataframe各科目均值"""
    df = data_frame()
    lines()
    df_mean = df.mean()
    print(f"dataframe的均值：\n{df_mean}")
    lines()
    df_std = round(df.std(), 2)
    print(f"dataframe的标准差：\n{df_std}")
    lines()
    df_median = df.median()
    print(f"dataframe的中位数：\n{df_median}")


@countdown
def cal_df_mean_col():
    df = data_frame()
    lines()
    df_mean_col = round(df.mean(axis="columns"), 2)
    print(f"dataframe所有科目均值：\n{df_mean_col}")


@countdown
def cal_df_mean_row():
    df = data_frame()
    lines()
    df_mean_row = round(df.mean(axis="rows"), 2)
    print(f"dataframe所有科目均值：\n{df_mean_row}")


@countdown
def find_df_achieved_student():
    """
        当我们写 df.loc[:, df.columns != "Name"] 时，
        我们实际上是在选择除了 "Name" 列之外的所有列。
        这是通过使用 df.columns != "Name" 来选择列标签，
        然后，使用 df.loc[:, ...] 来选择所有行。
        然后，我们使用 apply 方法对所选的列应用一个函数。
        在这种情况下，我们的函数是一个 lambda 函数 lambda x: x >= 60，
        它会将每个单元格的值与60进行比较，返回布尔值。
        因此，对于每个单元格，如果值大于或等于60，则返回 True，否则返回 False。
        这将导致整个 DataFrame 变为一个布尔型 DataFrame，其中每个单元格都是 True 或 False。
        接下来，我们调用 all(axis=1)，这会沿着列方向检查每行中的所有值。
        如果行中的所有值都为 True，则返回 True，否则返回 False。
        这样，我们最终得到一个布尔型 Series，
        其中每个元素表示相应行中的所有列是否都满足条件（大于或等于60）。
        最后，我们使用这个布尔型 Series 作为 DataFrame 的索引，
        过滤出满足条件的行。
        这意味着只有那些所有科目成绩都大于或等于60分的行会被保留在结果 DataFrame 中。
        """
    df = data_frame()
    lines()
    # 设置动态筛选条件，有一个不符合就是所有不符合
    df_bool = df.loc[:, df.columns != df.index.name].apply(lambda x: x >= 60).all(axis=1)
    df_achieved_student = df[df_bool]
    print(f"所有科目均达到60分及以上的学生：{len(df_achieved_student)} 人， 具体如下：\n{df_achieved_student}")
    lines()
    df_chinese_student = df[df.iloc[:, 0] >= 60]
    print(f"语文成绩大于或等于60分的学生：{len(df_chinese_student)} 人，具体如下：\n{df_chinese_student.iloc[:, 0]}")
    lines()
    df_english_student = df[df["English"] >= 60]
    print(f"英语成绩大于或等于60分的学生：{len(df_english_student)} 人，具体如下：\n{df_english_student["English"]}")


@countdown
def cal_df_add():
    """两组 DataFrame 相加"""
    df_01 = DataFrame(
        data=np.random.randint(0, 100, size=(3, 3)),
        index=["Tom", "Jerry", "Alice"],
        columns=["Chinese", "Mathmatics", "English"],
    )
    df_02 = DataFrame(
        data=np.random.randint(0, 100, size=(4, 4)),
        index=["Tom", "Jerry", "Alice", "Bob"],
        columns=["Chinese", "Mathmatics", "English", "Physics"],
    )
    df_result_with_nan = df_01 + df_02
    print(f"两组 DataFrame 相加、填充 NaN 的结果：\n{df_result_with_nan}")
    lines()
    df_result_without_nan = df_01.add(df_02, fill_value=0)
    print(f"两组 DataFrame 相加、不填充 NaN 的结果：\n{df_result_without_nan}")


@countdown
def data_frame_exercise_info():
    fake_data_len = 10
    random_min = 50
    random_max = 100
    index_name = [Faker().name() for _ in range(fake_data_len)]
    fake_dict_middle_term = {
        "Chinese": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Mathmatics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "English": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Physics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Chemistry": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Biology": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
    }
    df_middle_term = DataFrame(fake_dict_middle_term, index=index_name)
    print(df_middle_term)
    lines()
    fake_dict_final_term = {
        "Chinese": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Mathmatics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "English": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Physics": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Chemistry": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
        "Biology": [random.randint(random_min, random_max) for _ in range(fake_data_len)],
    }
    df_final_term = DataFrame(fake_dict_final_term, index=index_name)
    print(df_final_term)
    return df_middle_term, df_final_term


@countdown
def data_frame_exercise():
    df_middle_term, df_final_term = data_frame_exercise_info()
    lines()
    # 整合两组成绩，空值填充为0
    df_all_term = df_middle_term.add(df_final_term, fill_value=0)
    # 求学年平均值
    df_all_term_mean = df_all_term.mean() / 2
    print(f"学科平均值：\n{df_all_term_mean}")
    lines()
    # 求各科目平均值
    df_all_term_mean_col = round(df_all_term.mean(axis="columns") / 2, 2)
    print(f"学生总分平均值：\n{df_all_term_mean_col}")
    lines()
    # 求两组成绩的差值
    df_diff = df_final_term - df_middle_term
    print(f"期末与期中的成绩差值：\n{df_diff}")
    lines()
    # 求两组成绩的百分比变化
    df_percent_change = round(df_diff / df_middle_term * 100, 2)
    print(f"两组成绩的百分比变化：\n{df_percent_change}")
    lines()
    # 筛选出语文成绩大于60分的学生
    df_all_term_average = df_all_term / 2
    # 设置动态筛选条件
    df_bool = df_all_term_average.loc[:, df_all_term_average.columns != df_all_term_average.index.name].apply(lambda x: x >= 60).all(axis=1)
    df_chinese_student = df_all_term_average[df_bool]
    print(f"语文成绩大于60分的学生：{len(df_chinese_student)} 人，具体如下：\n{df_chinese_student.iloc[:, 0]}")
    lines()
    # 筛选出英语成绩大于60分的学生
    df_english_student = df_all_term_average[df_bool]
    print(f"英语成绩大于60分的学生：{len(df_english_student)} 人，具体如下：\n{df_english_student['English']}")


if __name__ == "__main__":
    array_calculation()
    cal_arr_sum_row()
    cal_arr_sum_col()
    data_frame()
    cal_df()
    cal_df_mean_col()
    cal_df_mean_row()
    find_df_achieved_student()
    cal_df_add()
    data_frame_exercise_info()
    data_frame_exercise()
