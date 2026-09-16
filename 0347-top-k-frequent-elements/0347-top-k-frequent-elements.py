
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap = []
        output = []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            count, num = heapq.heappop(heap)
            output.append(num)

        return output