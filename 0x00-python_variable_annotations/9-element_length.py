#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with\
the appropriate types
"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing the length of
    the sequence and the sequence itself.

    Args:
        lst: list of sequences

    Returns: list of tuples containing the length of the sequence and the sequence itself
    """
    return [(i, len(i)) for i in lst]
