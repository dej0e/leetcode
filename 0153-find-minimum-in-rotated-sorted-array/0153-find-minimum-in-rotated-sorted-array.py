class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min = -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # rotated - min should be in right half
                left = mid + 1 
            else:
                right = mid  # regular - min should be in left half
            
        return nums[left]
         