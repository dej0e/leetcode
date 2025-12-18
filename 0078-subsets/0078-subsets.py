class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(i):
            if i >= n:
                if path not in res:
                    res.append(path.copy())
                return
            
            # Adding current number to path
            path.append(nums[i])
            dfs(i+1)

            # Without adding current number to path
            path.pop()
            dfs(i+1)
                
        dfs(0)
        return res