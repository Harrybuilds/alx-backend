#!/usr/bin/env python3
"""
module that holds a function index_range and a class
Server.
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    function that takes 2 integer value as arguments
    and returns a tuple containing 2 integer value
    that represent the page number and the page_size
    respectively
    """
    return page * page_size - page_size, page * page_size


class Server:
    """
    Server class to paginate a database of popular
    baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method that takes two integer arguments page
        with default value 1 and page_size with default
        value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        full_dataset = self.dataset()

        page_details = index_range(page, page_size)

        page_contents = []

        try:
            for x in range(page_details[0], page_details[1]):
                page_contents.append(full_dataset[x])

            return page_contents
        except Exception as e:
            return page_contents

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        method that takes 2 integer value as argument and
        returns a dictionary containing more detailed data
        about a record
        """
        data_len = len(self.dataset())
        data = self.get_page(page, page_size)
        next_page = page + 1 if page in range(1, data_len) else None
        prev_page = page - 1 if page in range(2, data_len) else None
        total_pages = math.ceil(data_len / page_size)
        page_size = page_size if page in range(total_pages) else 0
        next_page = None if page_size == 0 else next_page

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
