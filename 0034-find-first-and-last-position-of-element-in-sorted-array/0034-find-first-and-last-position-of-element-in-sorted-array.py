class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        start_index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start_index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if start_index == -1:
            return [-1, -1]

        for i in range(start_index, len(nums)):
            if nums[i] != target:
                return [start_index, i - 1]

        return [start_index, len(nums) - 1]