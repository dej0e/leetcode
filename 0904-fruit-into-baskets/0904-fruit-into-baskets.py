class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        pick ={}
        l = r = 0
        maxlen = 0
        while r < len(fruits):
            pick[fruits[r]] = pick.get(fruits[r], 0) + 1
            if len(pick) > 2:
                while len(pick) > 2:
                    pick[fruits[l]] -= 1
                    if pick[fruits[l]] == 0:
                        del pick[fruits[l]]
                    l += 1
            else:
                maxlen = max(maxlen, r - l + 1)

            r += 1
        return maxlen