class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        res = []
        for i in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res