class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0 
        maxlen = 0
        count = defaultdict(int)
        while r < len(s):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count [s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen