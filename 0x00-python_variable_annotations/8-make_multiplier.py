#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takes a float multiplier 
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier.

    Args:
        multiplier: float to multiply by

    Returns: function that multiplies a float by multiplier
    """
    def mul(x: float) -> float:
        """The callable"""
        return x * multiplier
    return mul
