class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
                while r < len(numbers) - 1 and numbers[r] == numbers[r + 1]:
                    r -= 1
            elif sum < target:
                l += 1
                while l > 0 and numbers[l] == numbers[l - 1]:
                    l += 1
            else:
                return [l+1, r+1]
        return [-1, -1]
