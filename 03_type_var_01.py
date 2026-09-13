#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/7 12:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_type_var_01.py
# @Desc     :

from random import randint, uniform
from typing import TypeVar

Num = TypeVar("Num", int, float)


def identity[Num](num: Num) -> Num:
    return num


def main() -> None:
    """ Main Function """
    nums: list[int | float] = [randint(1, 100), uniform(1, 100)]
    for num in nums:
        print(f"{num} -> {identity(num)}")


if __name__ == "__main__":
    main()
