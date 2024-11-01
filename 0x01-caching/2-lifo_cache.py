#!/usr/bin/env python3
"""
module that defines the LIFOCache class
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    defines the LIFOCache class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        adds an item into the caching system if item
        is a new item, else update the item

        also remove item from caching system if length
        of items is greater than the MAX_ITEMS value
        using the LIFO algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = next(reversed(self.cache_data))
            print('DISCARD:', last_item)
            del self.cache_data[last_item]

        # add the item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        if key exist in cache system,
        returns the value in cache associated
        with the key else if key is not provided or
        key does not exist, returns None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
