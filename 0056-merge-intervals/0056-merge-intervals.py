class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for start, end in intervals:
            lastEnd = res[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start,end])
        return res 