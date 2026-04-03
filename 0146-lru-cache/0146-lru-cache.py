class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {} # key -> node
        self.capacity = capacity
        self.lru = Node(-1, -1)
        self.mru = Node(-1, -1)
        self.lru.next, self.mru.prev  = self.mru, self.lru


    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.next = node.prev = None
    
    def insert(self, node):
        prev = self.mru.prev 
        next = self.mru
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insert(self.cache[key])
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            popNode = self.lru.next
            self.remove(popNode)
            del self.cache[popNode.key]
        
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)