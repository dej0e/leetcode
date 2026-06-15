class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #Memoization
        # dp = [-1] * n
        # def houserob(ind):
        #     if ind == 0:
        #         return nums[0]
        #     if ind < 0:
        #         return 0
        #     if dp[ind] != -1:
        #         return dp[ind]

        #     pick = nums[ind]
        #     if ind > 1: 
        #         pick += houserob(ind - 2)
            
        #     notPick = 0 + houserob(ind - 1)

        #     dp[ind] = max(pick, notPick)
        #     return dp[ind]

        # return houserob(n-1)

        #Tabulation
        dp = [-1] * n
        dp[0] = nums[0]
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            
            notPick = 0 + dp[i - 1]
            dp[i] = max(pick, notPick)
        return dp[n-1]
