#!/usr/bin/env python3
"""
Caching LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching System using LIFO
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.lastIn = ''

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.lastIn]
                print(f'DISCARD: {self.lastIn}')
            self.lastIn = key

    def get(self, key):
        """
        return value linked to key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
