class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Choice to add nums[i] to subset
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            
            # Choice to exclude nums[i] from subset
            dfs(i + 1)

            
        dfs(0)

        return res
