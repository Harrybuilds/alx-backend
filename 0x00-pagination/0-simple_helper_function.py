#!/usr/bin/env python3
"""
module that holds an index_range functionthat returns
a tuple indicating the page number and the page size
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function that takes 2 integer value as arguments
    and returns a tuple containing 2 integer value
    that represent the page number and the page_size
    respectively
    """
    return page * page_size - page_size, page * page_size
