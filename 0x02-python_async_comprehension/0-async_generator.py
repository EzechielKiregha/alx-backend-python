#!/usr/bin/env python3
"""
this is a python
script that returns a
generator
"""


from asyncio import sleep
from typing import Generator
from random import random


async def async_generator() -> Generator[float, None, None]:
    """
    generators in python
    and asyncio
    """
    a: int = 1
    while a <= 10:
        await sleep(1)
        yield 10 * random()
        a += 1
