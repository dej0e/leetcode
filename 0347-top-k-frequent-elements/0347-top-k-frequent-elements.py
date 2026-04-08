class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = []
        heap = []
        for number, freq in count.items():
            heapq.heappush(heap, (-freq, number))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res