from enum import Enum


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        #bfs
        q = deque()
        q.append((0, -1))
        visited = set()
        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()
                visited.add(node)
                for neighbor in adj[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        return False # no cycles
                    q.append((neighbor, node))
        return len(visited) == n