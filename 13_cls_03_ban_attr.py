#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/16 23:52
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13_cls_03_ban_attr.py
# @Desc     :   

from inspect import currentframe
from random import randint

from access_modifiers import privatemethod, protectedmethod
from faker import Faker


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

    def __getattribute__(self, attr: str):
        if attr.startswith("_") and not (attr.startswith("__") and attr.endswith("__")):
            value = super().__getattribute__(attr)

            # Check if the attribute is a callable (method)
            if callable(value):
                return value

            # Check if the caller is the class itself
            caller_frame = currentframe().f_back
            caller_locals = caller_frame.f_locals
            is_internal_call = "self" in caller_locals and isinstance(caller_locals["self"], Bank)

            if not is_internal_call:
                raise AttributeError(
                    f"[Access Denied] "
                    f"{self.__class__.__name__!r} object attribute {attr!r} is private "
                    f"and cannot be accessed externally!"
                )

        return super().__getattribute__(attr)


def main() -> None:
    """ Main Function """
    account: str = Faker().credit_card_number()
    balance: int = randint(1_000, 9_999)

    bank = Bank(account, balance)
    bank.show_info()
    # print(bank._account)
    bank._get_account()


if __name__ == "__main__":
    main()
