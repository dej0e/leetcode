class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            if idx >= len(nums):
                return

            for i in range(0, len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                dfs(i, curr)
                curr.pop()
        dfs(0, [])
        return res