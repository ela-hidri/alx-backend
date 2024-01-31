#!/usr/bin/env python3
"""
Caching Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system  inherits from BaseCaching
    """
    def put(self, key, item):
        """
        add item to dict
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        return value linked to key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
