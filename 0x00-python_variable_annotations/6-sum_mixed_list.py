#!/usr/bin/env python3
"""
sum of integers and
floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this returns the sum of all
    the int and floats in the parameter
    array
    """
    return sum(mxd_lst)
