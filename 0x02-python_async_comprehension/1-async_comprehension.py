#!/usr/bin/env python3
"""
calling a yield on a next
that is the purpose of this
script
"""


from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    this is more about async
    python
    """
    return [i async for i in async_generator()]
