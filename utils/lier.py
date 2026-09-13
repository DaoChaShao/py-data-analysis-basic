#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/4 21:49
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   lier.py
# @Desc     :

from collections.abc import Generator
from contextlib import contextmanager
from enum import StrEnum, unique
from pathlib import Path
from typing import Any, Literal, Self

from faker import Faker
from pydantic import BaseModel, Field, field_validator, model_validator


@unique
class FakerTypes(StrEnum):
    CN = "zh_CN"
    EN = "en_GB"


def fake_info(
        language: str | Literal["zh_CN", "en_GB"] | FakerTypes,
        *,
        amount: int = 1,
        display: bool = True
) -> list[dict[str, str | int | float]]:
    """
    Generate fake information using the Faker library.

    :param language: The language to use for fake information.
    :param amount: The number of fake people to generate.
    :param display: Whether to print the generated people.
    :return: A list of dictionaries, each containing fake information about a person.
    """
    fake = Faker(language)
    people: list[dict[str, str | int | float]] = []
    for _ in range(amount):
        people.append({
            "name": fake.name(),
            "gender": fake.random_element(elements=(Gender.MALE.value, Gender.FEMALE.value)),
            "age": fake.random_int(min=1, max=100),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "address": fake.address(),
            "card": fake.credit_card_number(),
            "job": fake.job(),
        })
    if display:
        for person in people:
            print(person)
    return people


@unique
class Gender(StrEnum):
    MALE = "Male"
    FEMALE = "Female"


class PersonInfo(BaseModel):
    name: str
    gender: str | Gender
    age: int = Field(ge=18, le=65)
    job: str
    phone: str
    email: str
    address: str
    card: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email: {value!r} - missing '@' or '.'.")
        return value

    @model_validator(mode="after")
    def validate_email_format(self) -> Self:
        _domains: tuple[str, ...] = (".com", ".cn", ".org", ".net", ".edu")
        if not self.email.endswith(_domains):
            raise ValueError(f"Email must end with one of: {', '.join(_domains)}!")
        return self


class InfoIter:

    def __init__(self, language: str | Literal["zh_CN", "en_GB"] | FakerTypes, *, max_amount: int = 1) -> None:
        self._fake: Faker = Faker(language)
        self._amount: int = max_amount
        self._index: int = 0
        self._person: PersonInfo | None = None

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> PersonInfo:
        if self._index >= self._amount:
            raise StopIteration

        self._person = PersonInfo(
            name=self._fake.name(),
            gender=self._fake.random_element(elements=(Gender.MALE.value, Gender.FEMALE.value)),
            age=self._fake.random_int(min=18, max=65),
            job=self._fake.job(),
            phone=self._fake.phone_number(),
            email=self._fake.email(),
            address=self._fake.address(),
            card=self._fake.credit_card_number(),
        )
        self._index += 1
        return self._person

    def __len__(self) -> int:
        return self._amount

    def __repr__(self) -> str:
        return f"InfoIter(language={self._fake.locale!r}, max_amount={self._amount})"

    def __str__(self):
        if self._person is None:
            status = "Not Started!"
        else:
            status = f"{self._index}/{self._amount}"
        return f"<InfoIter: {self._amount} items, status: {status}>"


def generate_person(
        language: str | Literal["zh_CN", "en_GB"] | FakerTypes,
        *,
        max_amount: int = 1,
        display: bool = False
) -> Generator[PersonInfo, Any, None]:
    fake = Faker(language)
    for _ in range(max_amount):
        _person: PersonInfo = PersonInfo(
            name=fake.name(),
            gender=fake.random_element(elements=(Gender.MALE.value, Gender.FEMALE.value)),
            age=fake.random_int(min=18, max=65),
            job=fake.job(),
            phone=fake.phone_number(),
            email=fake.email(),
            address=fake.address(),
            card=fake.credit_card_number(),
        )
        if display:
            print(_person)
        yield _person


class TextReader:

    def __init__(
            self,
            filepath: str | Path,
            *,
            mode: str | Literal["r", "w", "a"] = "r",
            encoding: str = "utf-8",
            lazy: bool = True,
    ) -> None:
        self._filepath: Path = Path(filepath)
        self._mode: str = mode
        self._encoding: str = encoding
        self._lazy: bool = lazy
        self._file: Any | None = None

    def _read(self) -> str:
        if self._file is None:
            raise RuntimeError("File not opened!")
        return self._file.read()

    def _lazy_read(self) -> Generator[str, None, None]:
        if self._file is None:
            raise RuntimeError("File not opened!")
        for line in self._file:
            yield line.rstrip("\n")

    def __enter__(self) -> str | Generator[str, None, None]:
        self._file = open(self._filepath, self._mode, encoding=self._encoding)
        return self._lazy_read() if self._lazy else self._read()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self._file:
            self._file.close()


def read_text(
        filepath: str | Path,
        *,
        mode: str | Literal["r", "w", "a"] = "r",
        encoding: str = "utf-8",
        lazy: bool = True,
        display: bool = False
) -> str | Generator[str, Any, None]:
    match lazy:
        case True:
            def lazy_read() -> Generator[str, None, None]:
                with open(filepath, mode, encoding=encoding) as file:
                    for line in file:
                        _line = line.rstrip("\n")
                        if display:
                            print(_line)
                        yield _line

            return lazy_read()
        case False:
            with open(filepath, mode, encoding=encoding) as file:
                _content = file.read()
                if display:
                    print(_content)
                return _content
        case _:
            raise ValueError(f"Invalid lazy value: {lazy}!")


class TextIter:

    def __init__(
            self,
            filepath: str | Path,
            *,
            mode: str | Literal["r", "w", "a"] = "r",
            encoding: str = "utf-8",
    ) -> None:
        self._filepath: Path = Path(filepath)
        self._mode: str = mode
        self._encoding: str = encoding
        self._file: Any | None = None

    def __iter__(self) -> Self:
        if self._file is None:
            self._file = open(self._filepath, self._mode, encoding=self._encoding)
        return self

    def __next__(self) -> str:
        if self._file is None:
            raise RuntimeError("File not opened!")

        _line = next(self._file)
        return _line.rstrip("\n")

    def __enter__(self) -> Self:
        return iter(self)

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self._file is not None:
            self._file.close()
            self._file = None


@contextmanager
def load_text(
        filepath: str | Path,
        *,
        mode: str | Literal["r", "w", "a"] = "r",
        encoding: str = "utf-8",
        lazy: bool = True,
) -> str | Generator[str, None, None]:
    """
    Load text file with optional lazy loading.

    :param filepath: The path to the text file.
    :param mode: The mode in which the file is opened.
    :param encoding: The encoding of the file.
    :param lazy: Whether to load the file lazily.
    :return: A string or a generator of strings, depending on the lazy parameter.
    """
    with open(filepath, mode, encoding=encoding) as file:
        match lazy:
            case True:
                def lazy_read() -> Generator[str, None, None]:
                    for line in file:
                        yield line.rstrip("\n")

                yield lazy_read()
            case False:
                yield file.read()
