class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo: dict[int, bool] = {}

        def dfs(start_index):
            if start_index == len(s):
                memo[start_index] = True
                return True

            if start_index in memo:
                return memo[start_index]

            ans = False
            for word in wordDict:
                if s[start_index:].startswith(word):
                    ans = ans or dfs(start_index + len(word))

            memo[start_index] = ans
            return ans

        return dfs(0)
