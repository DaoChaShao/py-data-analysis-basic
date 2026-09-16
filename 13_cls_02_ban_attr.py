#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/16 23:15
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13_cls_02_ban_attr.py
# @Desc     :   

from inspect import currentframe
from random import randint

from access_modifiers import privatemethod, protectedmethod
from faker import Faker


def freeze(cls):
    """
    Freeze a class from external access to any attributes starting with _.

    :param cls: class to be frozen
    :return: the frozen class
    """
    original_getattribute = cls.__getattribute__

    def __getattribute__(self, attr):
        # Exclude magic methods (e.g., __init__, __str__ etc.)
        if attr.startswith("_") and not (attr.startswith("__") and attr.endswith("__")):
            # Get the caller's frame information
            caller_frame = currentframe().f_back
            caller_locals = caller_frame.f_locals

            # Determine if the caller is an internal call within the class
            is_internal_call = "self" in caller_locals and isinstance(caller_locals["self"], cls)

            if not is_internal_call:
                raise AttributeError(
                    f"[Access Denied] "
                    f"{self.__class__.__name__!r} object attribute {attr!r} is private "
                    f"and cannot be accessed externally!"
                )

        return original_getattribute(self, attr)

    cls.__getattribute__ = __getattribute__
    return cls


def block(cls):
    """
    Freeze a class from external access to any attributes and methods starting with _.

    :param cls: class to be frozen
    :return: the frozen class
    """
    original_getattribute = cls.__getattribute__

    def __getattribute__(self, attr):
        # Exclude magic methods (e.g., __init__, __str__ etc.)
        if attr.startswith("_") and not (attr.startswith("__") and attr.endswith("__")):
            # Get the attribute value using the original getattribute
            value = original_getattribute(self, attr)

            # Check if the attribute is a callable (method)
            if callable(value):
                return value

            # Get the caller's frame information
            caller_frame = currentframe().f_back
            caller_locals = caller_frame.f_locals

            # Determine if the caller is an internal call within the class
            is_internal_call = "self" in caller_locals and isinstance(caller_locals["self"], cls)

            if not is_internal_call:
                raise AttributeError(
                    f"[Access Denied] "
                    f"{self.__class__.__name__!r} object attribute {attr!r} is private "
                    f"and cannot be accessed externally!"
                )

        return original_getattribute(self, attr)

    cls.__getattribute__ = __getattribute__
    return cls


@block
class Bank:

    def __init__(self, account: str, balance: int):
        self._account: str = account
        self._balance: int = balance

    @protectedmethod
    def _get_account(self):
        return self._account

    @privatemethod
    def _get_balance(self):
        return self._balance

    def show_info(self):
        print(f"Card {self._account}'s balance is: {self._get_balance():,}.")


def main() -> None:
    """ Main Function """
    account: str = Faker().credit_card_number()
    balance: int = randint(1_000, 9_999)

    bank = Bank(account, balance)
    bank.show_info()
    # bank._get_account()
    # bank._get_balance()
    print(bank._account)


if __name__ == "__main__":
    main()
