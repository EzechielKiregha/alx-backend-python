#!/usr/bin/env python3
"""
the basics of a async io
a python module
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random delay
    and eventually returns it
    """
    value: float = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
