class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ## DP approach -- Bottom Up (Space optimised)
        # dp = [n for n in nums]
        # # dp[i] has sum until i
        # for i in range(1, n):
        #     dp[i] = max(dp[i], nums[i]+dp[i-1])
        # return max(dp)

        # Kadane's Algo -- sum below zero further reduces the sum, so reset the sum 
        # when negative sum encountered
        # curSum = 0
        # subMax = nums[0]
        # for i in range(len(nums)):
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += nums[i]
        #     subMax = max(subMax, curSum)
        # return subMax

        dp = []
        for i, num in enumerate(nums):
            dp.append(num)
        dp.append(-math.inf)
        
        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i], nums[i] + dp[i+1])
        return max(dp)