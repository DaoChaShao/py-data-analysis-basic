#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/16 22:54
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   13_cls_01_private.py
# @Desc     :   

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


class ANZ(Bank):

    def get_account(self):
        return self._get_account()

    def get_balance(self):
        return self._get_balance()


def main() -> None:
    """ Main Function """
    account: str = Faker().credit_card_number()
    balance: int = randint(1_000, 9_999)

    bank = Bank(account, balance)
    bank.show_info()
    # bank._get_account()
    # bank._get_balance()

    anz = ANZ(account, balance)
    print(anz.get_account())
    print(anz.get_balance())


if __name__ == "__main__":
    main()
