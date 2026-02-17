class Solution:
    def numDecodings(self, s: str) -> int:

        ## BOTTOM UP
        # n = len(s)
        # dp = {n: 1}
        # for i in range(n - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]

        #     if i + 1 < n and ((s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")):
        #         dp[i] += dp[i + 2]

        # return dp[0]

        ## TOP DOWN
        n = len(s)
        dp = {n: 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = 0
            res = dfs(i+1)
            if i+1 < n and ((s[i]=="1") or (s[i]=='2' and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return dp[i]
        return dfs(0)