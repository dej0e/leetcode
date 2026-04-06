class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res = ""
        n = len(s)
        i = 0
        while i < len(s):
            while i < n and s[i] == " ":
                i += 1

            if i < n:
                word_start = i
                while i < n and s[i] != " ":
                    i += 1
                word_end = i
                stack.append(s[word_start: word_end])
        
        return " ".join(reversed(stack))
