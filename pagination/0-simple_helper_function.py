#!/usr/bin/env python3
"""
Helper function for pagination.

This module provides a single function, `index_range`,
which calculates the start and end indexes for paginated data.
"""


def index_range(page, page_size):
    """
    Return a tuple containing a start and end index for a given page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
