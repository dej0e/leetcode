class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(i):
            if i >= n:
                if path not in res:
                    res.append(path.copy())
                return
            
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
                dfs(j+1)
        dfs(0)
        return res