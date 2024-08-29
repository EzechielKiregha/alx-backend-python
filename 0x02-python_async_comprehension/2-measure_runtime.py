#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
almost done
"""

import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    a coroutine to return
    the execution time
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()

    return end - start
