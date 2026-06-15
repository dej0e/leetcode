class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def houserob(ind):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]

            pick = nums[ind]
            if ind > 1: 
                pick += houserob(ind - 2)
            
            notPick = 0 + houserob(ind - 1)

            dp[ind] = max(pick, notPick)
            return dp[ind]

        return houserob(n-1)