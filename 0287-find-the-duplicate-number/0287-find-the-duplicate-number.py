class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for number in nums:
            idx = abs(number) - 1

            if nums[idx] < 0:
                return abs(number)
            
            nums[idx] = abs(nums[idx]) * -1
        return -1
