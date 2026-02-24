class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n for n in nums]
        # dp[i] has sum until i
        for i in range(1, n):
            dp[i] = max(dp[i], nums[i]+dp[i-1])
        return max(dp)
