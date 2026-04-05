from enum import Enum


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        q = deque() #node, parent
        q.append((0, -1))
        visited = set()
        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()
                
                if node in visited:
                    return False

                visited.add(node)
                for nei in adj[node]:
                    if nei == parent:
                        continue
                    q.append((nei, node))



        return True if len(visited) == n else False
