class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    continue
                path.append(candidates[j])
                dfs(j, path, total + candidates[j])
                path.pop()
        
        dfs(0, [], 0)
        return res