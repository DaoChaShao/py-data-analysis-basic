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
        #  Do not intercept Python magic methods / attributes
        if attr.startswith("__") and attr.endswith("__"):
            return super().__getattribute__(attr)

        if attr.startswith("_"):
            _value = super().__getattribute__(attr)

            # Check if the attribute is a callable (method)
            if callable(_value):
                return _value

            # Check if the caller is the class itself
            _frame = currentframe().f_back
            if _frame is not None:
                _caller_self = _frame.f_locals.get("self")
                if _caller_self is self:
                    return _value

            raise AttributeError(
                f"[Access Denied] "
                f"{type(self).__name__!r} object attribute "
                f"{attr!r} is private and cannot be accessed externally!"
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
