#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/4 22:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   01_iter_02.py
# @Desc     :

from pprint import pprint

from utils import FakerTypes, InfoIter


def main() -> None:
    """ Main Function """
    iterator: InfoIter = InfoIter(FakerTypes.CN.value, max_amount=1)
    pprint(next(iterator), sort_dicts=False)
    pprint(next(iterator), sort_dicts=False)


if __name__ == "__main__":
    main()
