class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score = 0
        for idx, num in enumerate(nums):
            heapq.heappush(heap, -num)
        
        for i in range(k):
            maxitem = -heapq.heappop(heap)
            score += (maxitem)
            maxitem = ceil (maxitem/ 3)
            heapq.heappush(heap, -maxitem)
        return score