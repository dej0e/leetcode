from enum import Enum


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        q = deque()
        q.append((0, -1))
        visited.add(0)
        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                q.append((neighbor, node))
                visited.add(neighbor)
        
        return True if len(visited) == n else False