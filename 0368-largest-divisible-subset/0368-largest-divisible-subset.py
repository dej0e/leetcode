class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[n] for n in nums]

        res = []
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dp[j]
                    if len(tmp) > len(dp[i]):
                        dp[i] = tmp
            if len(dp[i]) > len(res):
                res = dp[i]
        return res
