#!/usr/bin/env python3
"""
this is a module that
returns a turple from,
parameters
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple

    Args:
        k (str): k expect a string
        v (Union[int, float]): it expect either integer or float

    Returns:
        Tuple[str, float]: returns a tuple of either strings or floats
        maybe both
    """
    return (k, v ** 2)
