#!/usr/bin/env python3
"""
Caching FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching System using FIFO
    """
    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                old_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[old_key]
                print(f'DISCARD: {old_key}')

    def get(self, key):
        """
        return value linked to key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
