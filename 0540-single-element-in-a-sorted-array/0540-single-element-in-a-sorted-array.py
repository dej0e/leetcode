class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        l, h = 1, n - 2
        while l <= h:
            mid = l + ((h-l) // 2)
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:  
                # found the lone element
                return nums[mid]
            
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                # (even, odd) scenario, single element is on the right
                l = mid 
            else:
                # (odd, even) scenario, single element is on left half
                h = mid
        return -1