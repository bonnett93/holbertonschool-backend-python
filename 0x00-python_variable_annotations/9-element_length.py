#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple, List
"""
9-element_length
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Take an iterable sequence and return a list of tuples (i, lenth of i)
    """
    return [(i, len(i)) for i in lst]
