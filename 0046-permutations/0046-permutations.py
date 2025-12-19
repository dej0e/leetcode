class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        used = [False] * n
        def dfs(i):
            if i >= n:
                res.append(path[:])
                return
            
            for j in range(n):
                if used[j]:
                    continue
                nextnum = nums[j]
                path.append(nextnum)
                used[j] = True
                dfs(i+1)
                used[j] = False
                path.pop()
        dfs(0)
        return res
