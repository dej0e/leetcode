from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        counter: dict[str, int] = defaultdict(int)
        s_len = len(s)
        for right in range(s_len):
            counter[s[right]] += 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest