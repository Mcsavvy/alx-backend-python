#!/usr/bin/env python3
"""Annotations for lists."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats.

    Args:
        mxd_lst: list of floats

    Returns: sum of mxd_lst
    """
    return sum(mxd_lst)
