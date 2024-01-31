#!/usr/bin/env python3
"""
Caching MRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Caching System using MRU
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
                idx = len(self.ins) - 1
                del self.cache_data[self.ins[idx]]
                print(f'DISCARD: {self.ins[idx]}')
                self.ins.pop(idx)
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
