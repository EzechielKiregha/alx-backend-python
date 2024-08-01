#!/usr/bin/env python3
"""
complex annotations
for returning
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a type-annotated function element_length that
        takes in parameter lst: iterable sequence
        and returns a list of tuple sequence

    Args:
        lst (Iterable[Sequence]): list of iterables of sequence type

    Returns:
        List[Tuple[Sequence, int]]: a list of tuples of sequences and integers
    """

    return [(i, len(i)) for i in lst]
