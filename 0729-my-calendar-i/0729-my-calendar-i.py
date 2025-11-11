from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.calendar, (startTime, endTime)) # Gives leftmost index to insert
        if i > 0 and self.calendar[i-1][1] > startTime:
            return False
        if i < len(self.calendar) and endTime > self.calendar[i][0]:
            return False

        self.calendar.add((startTime,endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)