#!/usr/bin/env python3
"""Module for sum_mixed_list function."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats.

    Args:
        mxd_lst: List of integers and floats

    Returns:
        Sum as a float
    """
    return sum(mxd_lst)
