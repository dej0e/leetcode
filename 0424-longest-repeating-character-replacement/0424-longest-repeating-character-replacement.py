class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l, r = 0, 0
        maxlen = 0
        while r < len(s):
            hashmap[s[r]] += 1
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen
             