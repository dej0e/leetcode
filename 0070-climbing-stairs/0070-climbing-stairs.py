class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {i: -1 for i in range(1, n + 1)}
        cache[1] = 1
        cache[2] = 2
        if n in cache and cache[n] != -1:
            return cache[n]
        i = 3
        while i <= n:
            cache[i] = cache[i - 1] + cache[i - 2]
            i += 1
        return cache[n]
