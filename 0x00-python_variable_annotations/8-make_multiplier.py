#!/usr/bin/env python3
"""
a callable
python anotation
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    gets the multiplier and multiplies it to
    the float passed to the callable
    """
    return lambda x: x * multiplier
