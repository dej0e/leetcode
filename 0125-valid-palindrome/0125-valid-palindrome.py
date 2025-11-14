class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(arr) - 1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True