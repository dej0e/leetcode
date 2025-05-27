class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def is_palindrome(word):
            return word == word[::-1]

        def dfs(start_index, path):
            if start_index == n:
                res.append(path[:])
                return

            for end_index in range(start_index + 1, n + 1):
                prefix = s[start_index:end_index]
                if is_palindrome(prefix):
                    path.append(prefix)
                    dfs(end_index, path)
                    path.pop()

        dfs(0, [])
        return res
