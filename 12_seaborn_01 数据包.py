"""
Seaborn 附带的常用数据集包括：
https://github.com/mwaskom/seaborn-data
"""

import random
import seaborn as sns

sns_default_list = [
    "anagrams",
    "anscombe",
    "attention",
    "brain_networks",
    "car_crashes",
    "diamonds",
    "dots",
    "dowjones",
    "exercise",
    "flights",
    "fmri",
    "geyser",
    "glue",
    "healthexp",
    "iris",
    "mpg",
    "penguins",
    "planets",
    "seaice",
    "taxis",
    "tips",
    "titanic",
]
sns_default_dict = {
    "anagrams": "字母异位词数据集",
    "anscombe": "安斯库姆数据集",
    "attention": "注意力数据集",
    "brain_networks": "大脑网络数据集",
    "car_crashes": "汽车事故数据集",
    "diamonds": "钻石数据集",
    "dots": "点数据集",
    "dowjones": "道琼斯股票数据集",
    "exercise": "运动数据集",
    "flights": "航班数据集",
    "fmri": "磁共振成像数据集",
    "geyser": "喷泉数据集",
    "glue": "胶水数据集",
    "healthexp": "健康指标数据集",
    "iris": "鸢尾花数据集",
    "mpg": "汽车燃油效率数据集",
    "penguins": "企鹅数据集",
    "planets": "行星数据集",
    "seaice": "海冰数据集",
    "taxis": "出租车数据集",
    "tips": "小费数据集",
    "titanic": "泰坦尼克号数据集",
}
sns_random_sources = random.choice(list(sns_default_dict.keys()))
data = sns.load_dataset(sns_random_sources)
data_name = sns_default_dict[sns_random_sources]
print(f"{data_name} 的数据如下：\n{data.head(5)}")
print(f"{data_name} 的数据集形状：{data.shape}")
