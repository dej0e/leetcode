class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        for i in range(n-1, -1, -1):
            newDp = set()
            for ssum in dp:
                if ssum + nums[i] == target:
                    return True
                newDp.add(ssum + nums[i])
                newDp.add(ssum)
            dp = newDp
        return True if target in dp else False