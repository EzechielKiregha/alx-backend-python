#!/usr/bin/env python3
"""
this is a module that
returns a turple from,
parameters
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple
    """
    return (k, v ** 2)
