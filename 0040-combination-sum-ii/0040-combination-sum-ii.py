class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        n = len(candidates)
        def dfs(i, sum):
            if sum == target and path.copy() not in res:
                res.append(path.copy())
                return
            if i >= n or sum > target:
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                nextnum = candidates[j]
                if sum + nextnum > target:
                    break
                path.append(nextnum)
                dfs(j+1, sum+nextnum)
                path.pop()
        dfs(0, 0)
        return res