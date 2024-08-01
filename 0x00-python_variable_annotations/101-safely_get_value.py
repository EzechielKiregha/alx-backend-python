#!/usr/bin/env python3
"""
some modile on
advanced task
"""


from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    add types to this
    provided codes
    """
    if key in dct:
        return dct[key]
    else:
        return default
