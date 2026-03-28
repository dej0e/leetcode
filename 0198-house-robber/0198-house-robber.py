class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)
        # if len(nums) <= 2:
        #     return max(nums)
        
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return dp[-1]

        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2