class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l <= h:
            mid = l + ((h - l) // 2)
            sq = mid * mid
            if sq > x:
                h = mid - 1
            else:
                l = mid + 1
        return h