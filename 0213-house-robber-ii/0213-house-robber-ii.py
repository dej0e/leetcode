class Solution:
    def rob(self, nums: List[int]) -> int:
    
        if len(nums) == 1:
            return nums[0]
        withoutFirst = nums[1:]
        withoutLast = nums[:-1]
        return max(self.rob1(withoutFirst), self.rob1(withoutLast))

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            
            notPick = 0 + prev

            curri = max(pick, notPick)
            prev2 = prev
            prev = curri
        return prev

    