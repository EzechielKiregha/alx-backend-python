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
    This will spawn a wait_random
    n and return the number of
    delays sorted in asc

    Args:
        n (int): a number times which a specific delay is
        calculated
        max_delay (int): the specific delay

    Returns:
        List[float]:  list of the delays should be in ascending order
        without using sort() because of concurrency.
    """
    arrayList: List[float] = []
    for i in range(n):
        arrayList.append(await wait_random(max_delay))

    for i in range(n - 1):
        for j in range(n-1-i):
            if (arrayList[j] > arrayList[j + 1]):
                temp = arrayList[j]
                arrayList[j] = arrayList[j + 1]
                arrayList[j + 1] = temp

    return arrayList
