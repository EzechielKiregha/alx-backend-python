#!/usr/bin/env python3
"""
this is just to
add a new anotation
"""


from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element
    statically
    """
    if lst:
        return lst[0]
    else:
        return None
