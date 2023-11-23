#!/usr/bin/env python3
"""
Annotations, tuples
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of the int/float v.

    Args:
        k: string
        v: int or float

    Returns: tuple with k and the square of v
    """
    return (k, v ** 2)
