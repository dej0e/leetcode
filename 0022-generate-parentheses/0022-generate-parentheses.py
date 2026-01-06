class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, path, openn, close):
            if openn == close == n:
                res.append("".join(path))
                return
            
            if openn < n:
                path.append("(")
                dfs(i+1, path, openn + 1, close)
                path.pop()
            
            if close < openn:
                path.append(")")
                dfs(i+1, path, openn, close + 1)
                path.pop()
        dfs(0, [], 0, 0)
        return res