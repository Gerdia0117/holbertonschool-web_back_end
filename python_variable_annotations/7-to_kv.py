#!/usr/bin/env python3
"""Module for to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from string and squared number.

    Args:
        k: String key
        v: Integer or float value

    Returns:
        Tuple with string and squared value as float
    """
    return (k, v ** 2)
