#!/usr/bin/env python3
"""
9-element_length
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Take an iterable sequence and return a list of tuples (i, lenth of i)
    """
    return [(i, len(i)) for i in lst]
