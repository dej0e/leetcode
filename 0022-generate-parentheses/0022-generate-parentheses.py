class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(nopen, nclose):
            if nclose == nopen == n:
                res.append("".join(stack))
                return

            if nopen < n:
                stack.append("(")
                backtrack(nopen + 1, nclose)
                stack.pop()
            
            if nclose < nopen:
                stack.append(")")
                backtrack(nopen, nclose + 1)
                stack.pop()
            
            

        backtrack(0, 0)
        return res