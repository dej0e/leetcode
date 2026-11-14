class Solution:
    def totalFruit(self, arr: list[int]) -> int:
        map = {} # fruit type, frequency
        k = 2
        l = r = maxlen = 0
        while r < len(arr):
            map[arr[r]] = map.get(arr[r], 0) + 1
            if len(map) > k:
                # Unacceptable condition - more than 2 types of fruits collected
                map[arr[l]] -= 1
                if map[arr[l]] == 0:
                    del map[arr[l]]
                l += 1

            if len(map) <= k:
                # Acceptable condition - atmost 2 types of fruits collected
                maxlen = max(maxlen, r - l + 1)

            r += 1
        return maxlen