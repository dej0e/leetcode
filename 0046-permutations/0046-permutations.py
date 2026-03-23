class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if pick[i]:
                    continue
                
                pick[i] = True
                perm.append(nums[i])
                dfs(perm, pick)
                perm.pop()
                pick[i] = False
        dfs([], [False]*len(nums))
        return res
