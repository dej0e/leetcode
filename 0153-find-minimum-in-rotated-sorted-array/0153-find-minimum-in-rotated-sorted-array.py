class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float("infinity")
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[r]: # min is on the right side
                l = mid + 1
            else:
                r = mid - 1
        return res