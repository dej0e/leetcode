class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        water = [0]*len(height)

        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax: 
                l+=1
                leftMax = max(leftMax, height[l])
                water[l] = leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                water [r] = rightMax - height[r]
        return sum(water)