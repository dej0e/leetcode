class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l <= r:
            sum = numbers[l] + numbers[r]
            diff = target - sum

            if sum  > target:
                r = r - 1
            elif sum < target: 
                l = l + 1
            elif sum == target:
                return [l + 1, r + 1]
        
