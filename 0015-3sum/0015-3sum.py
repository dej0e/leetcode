class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for idx, a in enumerate(nums):
            if a > 0:
                break
            if idx > 0 and a == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r = r - 1
                elif threesum < 0:
                    l = l + 1
                elif threesum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
