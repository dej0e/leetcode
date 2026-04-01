class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [c.lower() for c in s if c.isalnum()]
        n = len(arr)
        l = 0
        r = n - 1
        m = l + ((r - l)//2)
        if n % 2: 
            l = r = m
        else:
            l = m 
            r = m + 1

        while l >= 0 and r < n:
            if arr[l] != arr[r]:
                return False
            
            l -= 1
            r += 1
        return True


