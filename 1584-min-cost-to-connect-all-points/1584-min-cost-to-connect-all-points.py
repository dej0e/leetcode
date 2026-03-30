class Solution:    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = self.calcManhattanDist(x1, y1, x2, y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        
        visited = set()
        minheap = []
        minheap.append((0, 0))
        cost = 0
        while len(visited) < len(points):
            dist1, node = heapq.heappop(minheap)
            if node in visited:
                continue
            
            cost += dist1
            visited.add(node)
            for neiCost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (neiCost, nei))

        return cost

    def calcManhattanDist(self, x1,y1,x2,y2) -> int:
        return abs((x1 - x2)) + abs((y1 - y2))       