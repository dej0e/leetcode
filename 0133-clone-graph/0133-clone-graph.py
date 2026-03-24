"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldNewMap = {}
        q = deque()
        q.append(node)
        newNode = Node(node.val)
        oldNewMap[node] = newNode

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldNewMap:
                    newNeiNode = Node(neighbor.val)
                    oldNewMap[neighbor] = newNeiNode
                    q.append(neighbor)
                oldNewMap[curr].neighbors.append(oldNewMap[neighbor])
        
        # for old, new in oldNewMap.items():
        #     for oneigh in old.neighbors:
        #         new.neighbors.append(oldNewMap[oneigh])
        return oldNewMap[node]

            