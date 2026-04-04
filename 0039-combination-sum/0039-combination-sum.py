class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                subset.append(candidates[j])
                dfs(j, subset, total + candidates[j])
                subset.pop()


        dfs(0, [], 0)
        return res
