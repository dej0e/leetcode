class Solution:
    def numDecodings(self, s: str) -> int:
        memo: dict[int, bool] = {}

        def dfs(start_index):
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1
            if s[start_index] == "0":
                return 0

            ways = 0
            ways += dfs(start_index + 1)
            if 10 <= int(s[start_index: start_index + 2]) <= 26:
                ways += dfs(start_index + 2)

            memo[start_index] = ways
            return ways

        return dfs(0)
