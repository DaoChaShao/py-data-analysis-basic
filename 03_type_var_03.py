#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/7 12:46
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_type_var_03.py
# @Desc     :

from typing import TypeVar

from faker import Faker
from pydantic import BaseModel

DataType = TypeVar("DataType", bound=BaseModel)


class ApiResponse[DataType](BaseModel):
    """ API Response with generic data type """
    code: int
    message: str
    data: DataType


class User(BaseModel):
    name: str
    age: int


def main() -> None:
    """ Main Function """
    fake = Faker()

    response = ApiResponse[User](
        code=fake.random_element(elements=(200, 404, 500)),
        message=fake.random_element(elements=("Success", "Error", "Warning")),
        data=User(name=fake.name(), age=fake.random_int(min=18, max=65))
    )

    print(response.code)
    print(response.message)
    print(response.data.name)
    print(response.data.age)


if __name__ == "__main__":
    main()
