class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 0

        l, h = 0, len(arr) - 1
        while l <= h:
            m = l + ((h - l) // 2)
            if m > 0 and arr[m] < arr[m-1]:
                h = m - 1
            elif m < len(arr) - 1 and arr[m] < arr[m + 1]:
                l = m + 1
            else:
                return m
        return -1