import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                diff = a - c
                if diff >= 0:
                    dp[a] = min(dp[a], 1 + dp[diff])

        return dp[amount] if dp[amount] != math.inf else -1
