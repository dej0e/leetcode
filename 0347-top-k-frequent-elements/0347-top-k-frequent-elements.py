class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (-count, num))
        res = []
        for i in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)
        return res