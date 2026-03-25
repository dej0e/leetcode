class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n

        def dfs(i):
            if visited[i] == True:
                return
            visited[i] = True
            for neighbor in adj[i]:
                dfs(neighbor)
        
        components = 0
        for i in range(n):
            if visited[i] != True:
                dfs(i)
                components += 1
        return components

        # visited = set()
        # def bfs(i):
        #     q = deque()
        #     q.append(i)
        #     visited.add(i)
        #     while q:
        #         node = q.popleft()
        #         for neighbor in adj[node]:
        #             if neighbor in visited:
        #                 continue
        #             q.append(neighbor)
        #             visited.add(neighbor)
        
        # components = 0
        # for i in range(n):
        #     if i not in visited:
        #         bfs(i)
        #         components += 1
        # return components

        