#!/usr/bin/python3
""" basic cach module """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class"""

    def put(self, key, item):
        """Put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        return self.cache_data.get(key)
