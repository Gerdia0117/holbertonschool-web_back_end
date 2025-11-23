#!/usr/bin/env python3
"""Module for make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier: Float to multiply by

    Returns:
        Function that multiplies a float by multiplier
    """
    def multiplier_func(x: float) -> float:
        """Multiply x by the multiplier."""
        return x * multiplier
    return multiplier_func
