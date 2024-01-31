#!/usr/bin/env python3
"""
Caching LFU caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Caching System using LFU
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.ins = {}

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                ss = sorted(self.ins.items(), key=lambda item: item[1])
                del self.cache_data[ss[0][0]]
                print(f'DISCARD: {ss[0][0]}')
                self.ins.pop(ss[0][0])
            if key in self.ins:
                self.ins[key] += 1
            self.ins[key] = 1

    def get(self, key):
        """
        return value linked to key
        """
        if key in self.cache_data:
            self.ins[key] += 1
            return self.cache_data[key]
        return None
