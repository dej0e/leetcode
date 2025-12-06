class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []
        def is_palindrome(s):
            return s == s[::-1]

        def dfs(start_index):
            if start_index == n:
                res.append(path.copy())
                return

            for end_index in range(start_index + 1, n + 1):
                prefix = s[start_index:end_index]
                if is_palindrome(prefix):
                    path.append(prefix)
                    dfs(end_index)
                    path.pop()
        dfs(0)
        return res
