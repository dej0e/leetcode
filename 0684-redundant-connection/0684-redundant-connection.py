class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n_edges = len(edges)
        n_vertices = n_edges + 1  
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        result = []
        visited = [False] * n_vertices
        cycle = set()
        cycleStart = -1
        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1,-1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []
                