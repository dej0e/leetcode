class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                # Do not allow the same number in the same recursion level. Skip it. 
                # In deeper recursion levels, this would work as at that point j == i.
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
               
                if total + candidates[j] > target:
                    break

                curr.append(candidates[j])
                dfs(j + 1, curr, total + candidates[j])
                curr.pop()
         
        dfs(0, [], 0)
        return res