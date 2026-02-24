class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ## DP approach -- Bottom Up (Space optimised)
        # dp = [n for n in nums]
        # # dp[i] has sum until i
        # for i in range(1, n):
        #     dp[i] = max(dp[i], nums[i]+dp[i-1])
        # return max(dp)

        curSum = 0
        subMax = nums[0]
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            subMax = max(subMax, curSum)
        return subMax