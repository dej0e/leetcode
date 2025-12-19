class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                if path not in res:
                    res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        dfs(0)
        return res