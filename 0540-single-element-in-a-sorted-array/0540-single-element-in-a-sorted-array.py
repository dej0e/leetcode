class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # “Is the single s at or to the left of index idx?”
        def is_single_on_or_before(idx: int) -> bool:
            if idx == len(nums) - 1:
                return True
            elif idx % 2 == 0:
                return nums[idx] != nums[idx + 1]
            else:
                return nums[idx] != nums[idx - 1]

        left, right = 0, len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if is_single_on_or_before(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[ans]
