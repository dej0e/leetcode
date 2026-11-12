class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        pick ={}
        k = 2 # two types only allowed
        l = r = 0
        maxlen = 0
        while r < len(fruits):
            pick[fruits[r]] = pick.get(fruits[r], 0) + 1
            if len(pick) > k:
                while len(pick) > k:
                    pick[fruits[l]] -= 1
                    if pick[fruits[l]] == 0:
                        del pick[fruits[l]]
                    l += 1
            else:
                maxlen = max(maxlen, r - l + 1)

            r += 1
        return maxlen