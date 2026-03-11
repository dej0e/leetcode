class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            leftHeight = height[l]
            rightHeight = height[r]
            maxArea = max(maxArea, min(leftHeight, rightHeight) * (r-l))
            if leftHeight > rightHeight:
                r -= 1
            else:
                l += 1
        return maxArea