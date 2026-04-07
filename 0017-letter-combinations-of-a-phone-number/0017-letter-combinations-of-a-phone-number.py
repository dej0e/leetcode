class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4":"ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        curr = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(curr))
                return
            
            for c in digit_map[digits[i]]:
                curr.append(c)
                dfs(i + 1)
                curr.pop()
                
        if digits:
            dfs(0)
        return res
            
