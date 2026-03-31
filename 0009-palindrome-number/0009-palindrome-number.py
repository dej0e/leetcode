class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        val = x
        p = 0
        i = 1
        while val > 0:
            digit = val % 10
            p = p*10 + digit
            val = val // 10
        return p == x