class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        res = []
        for r, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(r)

            while q[0] < l:
                q.popleft()
            
            if (r-l+1) == k:
                res.append(nums[q[0]])
                l+=1
        return res