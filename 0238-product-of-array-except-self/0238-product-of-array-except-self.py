class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left = 1
        for i in range(length):
            result[i] = left
            left *= nums[i]
        
        right = 1
        for i in reversed(range(length)):
            result[i] *= right
            right *= nums[i]
        return result