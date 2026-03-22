class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, currList, total):
            if total == target:
                res.append(currList.copy())
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                currList.append(candidates[j])
                dfs(j, currList, total + candidates[j])
                currList.pop()
        dfs(0, [], 0)
        return res