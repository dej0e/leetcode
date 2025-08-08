from enum import Enum


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # Both ways because undirected edge

        visited = set()

        def dfs(node, parent):
            # node is already been visited, CYCLE!
            if node in visited:
                return False
            visited.add(node)
            for neib in adj[node]:
                # Undirected edges (so it can happen that parent is a neighbor as well)
                if neib == parent:
                    continue
                if not dfs(neib, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        # Number of visited nodes should be same as total number of nodes in a tree.
        # Tree should not have a cycle, ie. dfs(x,y) = True!
