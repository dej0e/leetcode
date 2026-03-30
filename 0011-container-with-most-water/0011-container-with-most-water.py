class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            hl = height[l]
            hr = height[r]
            length = r - l
            h = min(hl, hr)
            max_area = max(max_area, length * h)
            if hl < hr:
                l += 1
            else:
                r -= 1
        return max_area