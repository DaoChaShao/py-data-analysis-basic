#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/10 20:03
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04_singleton_02_type.py
# @Desc     :   


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            # Method I
            # cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            # Method II
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Example(metaclass=Singleton):
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
