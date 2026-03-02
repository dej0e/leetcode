class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        minheap = []
        heapq.heappush(minheap, intervals[0][1])
        for interval in intervals[1:]:
            start, end = interval
            if minheap[0] <= start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
        return len(minheap)
