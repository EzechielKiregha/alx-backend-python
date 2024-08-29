#!/usr/bin/env python3
"""
module to execute multiple
coroutine at the same time
"""


import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this will spawn a wait_random
    n and return the number of
    delays sorted in asc
    """
    arr: List[float] = []
    for i in range(n):
        arr.append(await wait_random(max_delay))

    for i in range(n - 1):
        for j in range(n-1-i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr
