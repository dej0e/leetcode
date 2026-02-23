
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minheap = []
        intervals.sort(key=lambda x:x[0])
        for start,end in intervals:
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
        return len(minheap)