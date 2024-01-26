#!/usr/bin/env python3
"""
pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """
    stIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (stIndex, endIndex)
