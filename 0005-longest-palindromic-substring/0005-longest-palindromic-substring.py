class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # resIdx = -1
        # resLen = 0
        # dp = [[False] * n for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == True):
        #             dp[i][j] = True
        #             if (j - i + 1) > resLen:
        #                 resLen = j - i  + 1
        #                 resIdx = i

        # return s[resIdx : resIdx + resLen]

        n = len(s)
        res = ""
        resLen = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res