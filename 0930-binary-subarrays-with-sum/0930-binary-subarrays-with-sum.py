class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helper(goal):
            if goal < 0:
                return 0
            l = r = 0
            sum = 0
            res = 0
            while r < len(nums):
                sum += nums[r]
                while sum > goal:
                    sum -= nums[l]
                    l += 1
                
                res += (r - l + 1)
                r += 1
            return res
        

        return helper(goal) - helper(goal - 1)