class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        def dfs(i, sum):
            if sum == target:
                res.append(path[:])
                return
            if i == n or sum > target:
                return

            for j in range(i, n):
                nextnum = candidates[j]
                if sum + nextnum > target:
                    continue
                path.append(nextnum)
                dfs(j, sum + nextnum)
                path.pop()
        dfs(0, 0)
        return res