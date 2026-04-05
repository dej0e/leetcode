from enum import Enum


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque()  # node, parent
        visited = set()
        q.append((0, -1))
        visited.add(0)
        while q:
            node, parent = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, node))

        return len(visited) == n
