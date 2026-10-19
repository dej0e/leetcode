class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 0

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + ((high-low) // 2)
            if mid > 0 and arr[mid] < arr[mid - 1]:
                high = mid - 1
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                return mid
        return -1