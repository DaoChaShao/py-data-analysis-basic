#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/7 12:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   03_type_var_02.py
# @Desc     :

from typing import TypeVar

from faker import Faker
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


def process_model[ModelType](model: ModelType) -> ModelType:
    """ Process a model instance and return the same type """
    print(model.model_dump())
    return model


class User(BaseModel):
    name: str
    age: int


class Product(BaseModel):
    name: str
    price: float


def main() -> None:
    """ Main Function """
    fake = Faker()

    user: User = User(
        name=fake.name(),
        age=fake.random_int(min=18, max=65)
    )
    product: Product = Product(
        name=fake.random_element(["Apple", "Banana", "Cherry"]),
        price=fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.0, max_value=10.0)
    )

    process_model(user)
    process_model(product)
    process_model("hello")


if __name__ == "__main__":
    main()
