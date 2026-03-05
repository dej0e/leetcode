class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        end = 0
        lastIndex = defaultdict(lambda: -1)
        for idx, c in enumerate(s):
            lastIndex[c] = idx

        end = -1
        start = 0
        for i in range(len(s)):
            curr = s[i]
            end = lastIndex[curr] if lastIndex[curr] >= end else end
            if i == end:
                curr_size = end - start + 1
                res.append(curr_size)
                start = end + 1
                end = lastIndex[start]
        return res
