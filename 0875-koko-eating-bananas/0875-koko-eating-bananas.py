class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = l + ((r - l) // 2)
            total_time = 0 
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            
            if total_time <= h:
                ans = mid
                r = mid - 1
            elif total_time > h:
                l = mid + 1
        return ans