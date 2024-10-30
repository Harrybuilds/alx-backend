#!/usr/bin/env python3
"""
module that defines the FIFOCache class
that inherits from the BaseCaching
"""


from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    This class defines the FIFICache
    and is a caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        adds an item into the caching system if item
        is a new item, else update the item

        also remove item from caching system if length
        of items is greater than the MAX_ITEMS value
        using the FIFO algorithm
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                next_item = next(iter(self.cache_data.keys()))
                print('DISCARD', next_item)
                del self.cache_data[next_item]

    def get(self, key):
        """
        if key exist in cache system,
        returns the value in cache associated
        with the key else if key is not provided or
        key does not exist, returns None
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
        
