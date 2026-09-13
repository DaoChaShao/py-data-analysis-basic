#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/10 20:37
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04_singleton_03_new.py
# @Desc     :   

from threading import Lock


class Singleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            print("Initialized")


class Example(Singleton):
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
