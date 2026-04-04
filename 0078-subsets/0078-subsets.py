class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i] (remove from subset, because we added it above.)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res