class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = math.inf
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                # left side is sorted
                res = min(res, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[r]:
                # right side is sorted
                res = min(res, nums[mid])
                r = mid - 1
        return res