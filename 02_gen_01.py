#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/4 23:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   02_gen_01.py
# @Desc     :

from pprint import pprint

from utils import FakerTypes, generate_person


def main() -> None:
    """ Main Function """
    people = generate_person(FakerTypes.CN.value, max_amount=2, display=False)
    print(people)
    pprint(next(people), sort_dicts=False)
    pprint(next(people), sort_dicts=False)
    pprint(next(people), sort_dicts=False)


if __name__ == "__main__":
    main()
