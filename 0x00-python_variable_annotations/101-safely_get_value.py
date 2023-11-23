#!/usr/bin/env python3
"""Using TypeVar and typing for dicts"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Returns the value of a key in a dict.

    Args:
        dct: dict
        key: key to look for
        default: default value to return if key does not exist

    Returns: value of key or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
