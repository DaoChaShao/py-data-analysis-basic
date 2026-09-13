#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/10 21:45
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   05_protocol.py
# @Desc     :   

from faker import Faker
from typing import Protocol, runtime_checkable


@runtime_checkable
class Greeter(Protocol):
    
    def greet(self) -> None: ...


class EnglishGreeter:

    def __init__(self, name: str):
        self._name: str = name

    def greet(self) -> None:
        print(f"Hello, {self._name}!")


class ChineseGreeter:

    def __init__(self, name: str):
        self._name: str = name

    def greet(self) -> None:
        print(f"你好，{self._name}！")


class FakeGreeter:
    def __init__(self, name: str):
        self._name: str = name

    # def greet(self) -> str:
    def greeting(self) -> str:
        """
        Fake greet
        Signature unmatches, return type is str. However, runtime_checkable does not check return type

        :return: String
        :rtype: str
        """
        return f"oops! {self._name}"


def welcome(greeter: Greeter) -> None:
    greeter.greet()


def main() -> None:
    """ Main Function """
    fake: Faker = Faker()
    name: str = fake.name()
    english_greeter: EnglishGreeter = EnglishGreeter(name)
    chinese_greeter: ChineseGreeter = ChineseGreeter(name)
    fake_greeter: FakeGreeter = FakeGreeter(name)

    print(isinstance(english_greeter, Greeter))  # True
    print(isinstance(chinese_greeter, Greeter))  # True
    print(isinstance(fake_greeter, Greeter))  # False

    welcome(english_greeter)
    welcome(chinese_greeter)
    welcome(fake_greeter)


if __name__ == "__main__":
    main()
