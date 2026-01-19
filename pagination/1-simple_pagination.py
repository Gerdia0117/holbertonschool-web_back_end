#!/usr/bin/env python3
"""
Simple pagination module
"""

import csv
from typing import List, Tuple
import os

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start index and end index for pagination.

    Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    # Use absolute path to CSV so it always works
    DATA_FILE = os.path.join(os.path.dirname(__file__), "Popular_Baby_Names.csv")

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        # Validate input
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # If start_index out of range, return empty list
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

