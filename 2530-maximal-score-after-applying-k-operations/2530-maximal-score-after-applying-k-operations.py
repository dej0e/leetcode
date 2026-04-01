class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score = 0
        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, idx))
        
        for i in range(k):
            maxitem, idx= heapq.heappop(heap)
            score += (-maxitem)
            nums[idx] = ceil (nums[idx] / 3)
            heapq.heappush(heap, (-nums[idx], idx))
        return score