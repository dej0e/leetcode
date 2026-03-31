class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {} # map key to Node
        self.capacity = capacity
        self.left = Node(0,0) # LRU
        self.right = Node(0,0) # most recent
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node): #remove node from list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): #insert at right 
        right = self.right
        prev = self.right.prev
        node.next = right
        node.prev = prev
        prev.next = node
        right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
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