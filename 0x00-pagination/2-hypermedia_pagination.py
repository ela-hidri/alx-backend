#!/usr/bin/env python3
"""
Pagination
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """
    stIndex = (page - 1) * page_size
    endIndex = page * page_size
    return (stIndex, endIndex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the appropriate page of the dataset
        """
        assert isinstance(page_size, int) and isinstance(page, int)
        assert page_size > 0 and page > 0

        row = index_range(page, page_size)
        dataset = self.dataset()
        if row and dataset:
            st = row[0]
            end = row[1]
            return dataset[st:end]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        creates a dictionary
        """
        dict = {}
        dict['page_size'] = page_size
        dict['page'] = page
        dict['data'] = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        dict['next_page'] = page + 1 if page + 1 < total_pages else None
        dict['prev_page'] = page - 1 if page - 1 > 0 else None
        dict['total_pages'] = total_pages
        return dict
