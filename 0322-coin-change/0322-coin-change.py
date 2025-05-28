from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount +1)

        def dfs(sum):
            if sum == amount:
                return 0
            if sum > amount:
                return inf

            if memo[sum] != -1:
                return memo[sum]

            ans = inf
            for coin in coins:
                result = dfs(sum + coin)
                if result != inf:
                    ans = min(ans, result + 1)

            memo[sum] = ans
            return ans

        result = dfs(0)
        return result if result != inf else -1
