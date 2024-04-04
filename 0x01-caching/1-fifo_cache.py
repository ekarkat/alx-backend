#!/usr/bin/python3
""" Task 2 Doc """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Fifo class"""

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Put method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data.items()))
                self.cache_data.pop(removed[0])
                print("DISCARD:", removed[0])
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        return self.cache_data.get(key)
