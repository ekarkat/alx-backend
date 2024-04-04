#!/usr/bin/python3
""" Task 2 modul """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """init mehoid super"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Put method"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Get method"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
