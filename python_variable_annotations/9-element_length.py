#!/usr/bin/env python3
"""Module for element_length function."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get length of each element in an iterable.

    Args:
        lst: Iterable of sequences

    Returns:
        List of tuples with sequence and its length
    """
    return [(i, len(i)) for i in lst]
