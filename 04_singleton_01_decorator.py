#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/10 19:49
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04_singleton_01_decorator.py
# @Desc     :   

from functools import wraps


def singleton(cls):
    """ Singleton Decorator """
    _instances: dict = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper


@singleton
class Example:
    """ Example Class """
    pass


def main() -> None:
    """ Main Function """
    left = Example()
    right = Example()

    print(left is right)  # True
    print(id(left), id(right))  # same id
    print(type(Example))  # <class '__main__.Singleton'>
    print(type(left))  # <class '__main__.Example'>

    assert left is right


if __name__ == "__main__":
    main()
