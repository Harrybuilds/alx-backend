#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert isinstance(index, int)
        next_index =
        
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': self.get_page(index, page_size)
        }


server = Server()
print(server.indexed_dataset())
