from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            if len(point) < 2:
                continue  # skip point dist calc
            x1 = point[0]
            y1 = point[1]
            dist = (x1**2) + (y1**2)  # because origin = 0,0
            heapq.heappush(heap, (dist, x1, y1))
        res = []
        
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res
