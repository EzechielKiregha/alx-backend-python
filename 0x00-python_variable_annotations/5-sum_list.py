#!/usr/bin/env python3
"""
takes in a list of floats
and returns their
sum
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """this function returns
    a sum of values in the list

    Args:
        input_list (List[float]): element of this list is expected
        to be a float otherwise type error is raised by type system

    Returns:
        float: the sum of all elements in input list
    """
    return sum(input_list)
