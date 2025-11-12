class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            # left portion is sorted
            if nums[left] <= nums[mid]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1


            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1