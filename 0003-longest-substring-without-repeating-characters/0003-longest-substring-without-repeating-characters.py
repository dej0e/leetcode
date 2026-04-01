from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        r = 0
        longest = 0
        for r in range(len(s)):

            if s[r] in map:
                l = max(l, map[s[r]] + 1)
            map[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
        

                
