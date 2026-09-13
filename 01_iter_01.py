#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/4 21:55
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   01_iter_01.py
# @Desc     :

from pprint import pprint
from random import randint

from utils import fake_info


def main() -> None:
    """ Main Function """
    language: str = "zh_CN" if randint(0, 1) else "en_GB"
    data = fake_info(language, amount=3)
    # pprint(data, sort_dicts=False)

    iterator = iter(data)
    pprint(next(iterator), sort_dicts=False)
    pprint(next(iterator), sort_dicts=False)


if __name__ == "__main__":
    main()
