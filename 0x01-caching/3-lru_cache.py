#!/usr/bin/env python3
"""
Caching LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Caching System using LRU
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.ins = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.ins[0]]
                print(f'DISCARD: {self.ins[0]}')
                self.ins.pop(0)
            if key in self.ins:
                self.ins.pop(self.ins.index(key))
            self.ins.append(key)

    def get(self, key):
        """
        return value linked to key
        """
        if key in self.cache_data:
            self.ins.pop(self.ins.index(key))
            self.ins.append(key)
            return self.cache_data[key]
        return None
