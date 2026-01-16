class LRUCache:
    cached = None
    capacity = -1
    last_key = -1
    def __init__(self, capacity: int):
        self.cached = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.last_key = key
        if key not in self.cached:
            return -1
        self.cached.move_to_end(key)
        return self.cached[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cached:
            self.cached.move_to_end(key)
        self.cached[key] = value
        if len(self.cached) > self.capacity:
            self.cached.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)