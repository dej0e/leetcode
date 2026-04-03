class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = defaultdict(int)

        if k == 0:
            return 0
        for c in s:
            count[c] += 1
        
        if min(count.values()) < k:
            return -1
        if len(count) < 3:
            return -1
        l = 0
        res = float("inf")
        for r in range(len(s)):
            count[s[r]] -= 1
            while min(count.values()) < k:
                count[s[l]] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res
