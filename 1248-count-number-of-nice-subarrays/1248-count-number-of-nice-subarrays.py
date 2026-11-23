class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atmost(k: int):
            l = r = 0
            res = 0
            add = 0
            if k < 0:
                return 0
            while r < len(nums):
                add += nums[r] % 2
                while add > k:
                    add -= nums[l] % 2
                    l += 1
                res = res + (r - l + 1)
                r += 1
            return res

        return atmost(k) - atmost(k - 1)
