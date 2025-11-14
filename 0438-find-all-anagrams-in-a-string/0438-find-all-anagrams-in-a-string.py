class Solution:
    def findAnagrams(self, original: str, check: str) -> List[int]:
        original_len = len(original)
        check_len = len(check)
        if original_len < check_len:
            return []
        check_counter = [0] * 26
        window_counter = [0] * 26
        a = ord("a")
        res = []
        # Starting window
        for i in range(check_len):
            check_counter[ord(check[i]) - a] += 1
            window_counter[ord(original[i]) - a] += 1
        if check_counter == window_counter:
            res.append(0)
        
        # Sliding window
        for i in range(check_len, original_len):
            window_counter[ord(original[i - check_len]) - a] -= 1
            window_counter[ord(original[i]) - a] += 1
            if check_counter == window_counter:
                res.append(i - check_len + 1)
        
        return res