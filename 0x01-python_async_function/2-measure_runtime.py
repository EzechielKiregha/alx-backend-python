#!/usr/bin/env python3
"""
this is for mesearing the
run time of the coroutine
"""


import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    the executioin time divided by
    n will be the float returned
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
