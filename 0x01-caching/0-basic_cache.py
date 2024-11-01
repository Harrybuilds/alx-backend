#!/usr/bin/env python3
"""
module that defines the BasicCache class
which inherits from the base class BaseCaching
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that defines the caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
    # raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
    # raise NotImplementedError("get must be implemented in your cache class")
