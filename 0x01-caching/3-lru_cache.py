#!/usr/bin/env python3
"""
module that defines the LRUCache class
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system following the Least Recently Used (LRU) principle.
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item in the cache. If the cache exceeds
        the maximum allowed items,
        removes the least recently used item
        according to the LRU algorithm.
        """
        if key is None or item is None:
            return

        """ 
        If key is already in cache,
        move it to the end to mark as recently used
        """
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value

        # Add the item to the cache
        self.cache_data[key] = item

        # If the cache exceeds the maximum size, pop the first (least recently used) item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the least recently used item (first item in OrderedDict)
            lru_key, _ = self.cache_data.popitem()
            print("DISCARD:", lru_key)

    def get(self, key):
        """
        Retrieve an item from the cache by key. If accessed, mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end to mark it as recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return self.cache_data[key]
