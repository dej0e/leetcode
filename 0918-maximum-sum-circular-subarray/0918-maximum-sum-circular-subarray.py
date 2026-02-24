class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = globalMin = nums[0]
        curMax = curMin = 0
        total = 0
        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        return max(total - globalMin, globalMax) if globalMax > 0 else globalMax