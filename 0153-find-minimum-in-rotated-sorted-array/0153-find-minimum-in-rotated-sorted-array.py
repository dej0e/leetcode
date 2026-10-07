class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = math.inf
        l, r = 0, len(nums) - 1
        while l <= r:
            res = min(res, nums[l])
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                # left side is sorted
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid - 1
        return res