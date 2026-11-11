class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxlen = 0
        l = r = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                length =  r - l + 1
                maxlen = max(maxlen, length)

            r += 1
        return maxlen