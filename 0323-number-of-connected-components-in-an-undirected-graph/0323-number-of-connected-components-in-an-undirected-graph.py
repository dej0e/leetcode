class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = [False] * n
        components = 0

        def bfs(node):
            nonlocal components
            q = deque([node])
            visited[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if visited[nei]:
                        continue
                    visited[nei] = True
                    q.append(nei)
            components += 1

        for i in range(n):
            if visited[i] == False:
                bfs(i)
        return components
