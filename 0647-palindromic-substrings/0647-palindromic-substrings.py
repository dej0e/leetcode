class Solution:
    def countSubstrings(self, s: str) -> int:
        # n = len(s)
        # res = 0
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]==True):
        #             dp[i][j] = True
        #             res += 1
        # return res


        def countPali(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        res = 0 
        for i in range(len(s)):
            l, r = i, i
            res += countPali(l, r)

            l, r = i, i + 1
            res += countPali(l, r)
        return res
