class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)
            if x != y:
                y = -1 * (y - x)
                heapq.heappush(heap, y)
        heap.append(0)
        return -1 * heap[0]
