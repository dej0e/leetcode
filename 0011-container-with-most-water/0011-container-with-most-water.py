class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calcArea(left: int, leftVal: int, right: int, rightVal:int):
            return min(leftVal, rightVal) * (right - left)
        
        left, right = 0, len(height) - 1
        maxArea = 0
        while left <= right:
            current_area = calcArea(left, height[left], right, height[right])
            maxArea = max(maxArea, current_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
