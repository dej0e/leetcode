class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = -math.inf
        for n in nums:
            temp = curMax * n

            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(curMax, res)
        return res