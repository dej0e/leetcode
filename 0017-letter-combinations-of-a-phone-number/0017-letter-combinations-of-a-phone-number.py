class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        KEYBOARD = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res: List[str] = []
        if not digits:
            return []
        def dfs(start_index, path):
            if start_index == len(digits):
                res.append("".join(path))
                return

            next_number = digits[start_index]
            for letter in KEYBOARD[next_number]:
                path.append(letter)
                dfs(start_index + 1, path)
                path.pop()

        dfs(0, [])
        return res
