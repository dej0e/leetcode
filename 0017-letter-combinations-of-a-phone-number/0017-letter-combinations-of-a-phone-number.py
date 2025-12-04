class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(start_index, path):
            if start_index == len(digits):
                res.append("".join(path))
                return
            next_number = digits[start_index]
            for letter in digit_map[next_number]:
                path.append(letter)
                dfs(start_index + 1, path)
                path.pop()

        dfs(0, [])
        return res
