class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0 
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]
        water = [0] * (n)
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                water[l] = leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                water[r] = rightMax - height[r]
        return sum(water)