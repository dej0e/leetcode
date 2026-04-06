class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIdx = -1
        resLen = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == True):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = j - i  + 1
                        resIdx = i



        return s[resIdx : resIdx + resLen]