#!/usr/bin/env python3
"""
8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.
    """
    def multi_floats(number: float) -> float:
        """
        multiplies a float by multiplier.
        """
        return number * multiplier

    return multi_floats
