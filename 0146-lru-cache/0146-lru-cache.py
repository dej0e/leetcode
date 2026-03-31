class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {} # map key -> node
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left 


    def remove(self, node): # Remove from list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.next = node.prev = None

    def insert(self, node): #Insert at rightmost end (MRU)
        nxt = self.right
        prev = self.right.prev
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        return -1    
    
    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)