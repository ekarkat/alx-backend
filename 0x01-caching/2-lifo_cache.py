#!/usr/bin/python3
""" Task 2 modul """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFO class"""

    def __init__(self):
        """init mehoid super"""
        super().__init__()

    def put(self, key, item):
        """Put method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        return self.cache_data.get(key)
