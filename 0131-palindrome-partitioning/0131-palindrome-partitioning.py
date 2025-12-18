class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def is_palindrome(word:str):
            return word == word[::-1]

        def dfs(i, part):
            if i >= n:
                res.append(part.copy())
                return

            for j in range(i, n):
                prefix = s[i:j+1]
                if not is_palindrome(prefix):
                    continue
                part.append(prefix)
                dfs(j+1, part)
                part.pop()

        dfs(0,[])
        return res