#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2026/9/10 20:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   04_singleton_04_logger.py
# @Desc     :   

from logging import getLogger, Formatter, INFO, StreamHandler
from threading import Lock
from typing import Optional


class Logger:
    _instance: Optional["Logger"] = None
    _lock: Lock = Lock()
    _initialised: bool = False
    _count: int = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, logger_name: str = "myapp"):
        with Logger._lock:
            if Logger._initialised:
                return
            Logger._initialised = True
            Logger._count += 1
            print(f"__init__ called {Logger._count}")

            self._logger = getLogger(logger_name)
            self._logger.setLevel(INFO)
            self._init_handler()

    def _init_handler(self):
        """ Initialize handler """
        if not self._logger.handlers:
            handler = StreamHandler()
            handler.setFormatter(Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self._logger.addHandler(handler)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)


def main() -> None:
    """ Main Function """
    a = Logger()
    b = Logger()
    print(a is b)  # True

    a.info("hello")
    b.error("oops")


if __name__ == "__main__":
    main()
