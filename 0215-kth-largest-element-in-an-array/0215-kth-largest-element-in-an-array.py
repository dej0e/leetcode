class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        negNums = [-n for n in nums]
        heap = negNums
        heapq.heapify(heap)
        value = -1
        for i in range(k):
            value = -heapq.heappop(heap)
        return value