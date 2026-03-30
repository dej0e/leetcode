class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        visited = set()
        minheap = [(0, k)]
        time = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            
            time = w1
            visited.add(n1)

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, (w1 + w2, n2))

        return time if len(visited) == n else -1
