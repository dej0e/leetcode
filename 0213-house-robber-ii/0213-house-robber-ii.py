class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        n = len(nums)
        return max(self.houseRob(nums[: n - 1]), self.houseRob(nums[1:n]))
    
    def houseRob(self, nums) -> int:
        if len(nums) == 1:
            return nums[-1]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n-1]
