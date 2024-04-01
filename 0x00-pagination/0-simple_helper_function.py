#!/usr/bin/env python3
""" Documentation """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
