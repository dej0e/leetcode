class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, curr, picked):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if picked[i]:
                    continue
                curr.append(nums[i])
                picked[i] = True
                dfs(i, curr, picked)
                picked[i] = False
                curr.pop()

        dfs(0, [], [False]*len(nums))
        return res