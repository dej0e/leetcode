class Solution:
    def feasible(self, piles: List[int], h:int, k: int):
        if k == 0:
            return False
        hours_used = 0
        for p in piles:
            hours_used += ceil(float(p)/k)
        return hours_used <= h
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, 1000000000
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.feasible(piles, h, mid):
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans

