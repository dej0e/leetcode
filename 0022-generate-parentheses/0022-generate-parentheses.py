class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, path, open, close):
            if i == n*2:
                res.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                dfs(i+1, path, open+1, close)
                path.pop()
            
            if close < open:
                path.append(")")
                dfs(i+1, path, open, close+1)
                path.pop()
            
        dfs(0, [], 0, 0)
        return res