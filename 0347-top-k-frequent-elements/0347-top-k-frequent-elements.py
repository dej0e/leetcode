class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        minheap = []
        for key, value in count.items():
            heapq.heappush(minheap, (value, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res