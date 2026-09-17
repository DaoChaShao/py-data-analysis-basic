#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/17 13:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13_cls_04_cls.py
# @Desc     :

from inspect import currentframe
from random import randint

from access_modifiers import privatemethod, protectedmethod
from faker import Faker


class Access:

    def __getattribute__(self, attr: str):
        """
        Override __getattribute__ to control attribute access

        :param attr: The attribute name to access
        :return: The attribute value if accessible, otherwise raise AttributeError
        """
        if attr.startswith("__") and attr.endswith("__"):
            return super().__getattribute__(attr)

        if not attr.startswith("_"):
            return super().__getattribute__(attr)

        _value = super().__getattribute__(attr)

        if callable(_value):
            return _value

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


class Bank(Access):

    def __init__(self, account: str, balance: int):
        self._account: str = account
        self._balance: int = balance

    @protectedmethod
    def _get_account(self):
        return self._account

    @privatemethod
    def _get_balance(self):
        return self._balance

    @property
    def account(self):
        return self._get_account()

    @property
    def balance(self):
        return self._get_balance()

    def show_info(self):
        print(f"Card {self._account}'s balance is: {self._get_balance():,}.")


def main() -> None:
    """ Main Function """
    account: str = Faker().credit_card_number()
    balance: int = randint(1_000, 9_999)

    bank = Bank(account, balance)
    print(bank.account)
    print(bank._account)


if __name__ == "__main__":
    main()
