class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, subset):

            res.append(subset.copy())
            if i >= len(nums):
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()
        dfs(0, [])
        return res                