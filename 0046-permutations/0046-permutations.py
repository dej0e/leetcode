class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        visited = set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in visited:
                    continue
                path.append(nums[j])
                visited.add(nums[j])
                dfs(path)
                path.pop()
                visited.remove(nums[j])
        dfs([])
        return res