class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = set()
        dp.add(0)
        for i in range(n - 1, -1, -1):
            new_dp = set()
            for subsum in dp:
                if subsum + nums[i] == target:
                    return True
                new_dp.add(subsum + nums[i])
                new_dp.add(subsum)
            dp = new_dp
        return True if target in dp else False