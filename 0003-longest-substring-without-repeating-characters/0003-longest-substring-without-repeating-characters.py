from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        count: Dict[str, int] = dict()
        s_len = len(s)
        for right in range(left, s_len):
            count[s[right]] = count.get(s[right], 0) + 1
            while count[s[right]] > 1:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest

            