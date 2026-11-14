class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        map = {}
        l = r = maxlen = 0
        while r < len(s):
            map[s[r]] = map.get(s[r], 0) + 1
            if len(map) > k:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1
            
            if len(map) <= k:
                maxlen = max(maxlen, r - l + 1)
            r += 1
        return maxlen