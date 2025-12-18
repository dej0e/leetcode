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
            
            
            dfs(i+1)
            
            # Adding current number to path
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            
                
        dfs(0)
        return res