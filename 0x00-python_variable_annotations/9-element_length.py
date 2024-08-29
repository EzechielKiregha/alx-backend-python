#!/usr/bin/env python3
"""
complex annotations
for returning
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        a type-annotated function element_length that
        takes in parameter lst: iterable sequence
        and returns a list of tuple sequence
    """

    return [(i, len(i)) for i in lst]
