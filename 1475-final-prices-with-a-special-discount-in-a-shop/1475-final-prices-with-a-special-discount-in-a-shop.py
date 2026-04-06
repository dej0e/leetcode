class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [price for price in prices]
        stack = [] # indexes, values increasing order monotonic increase
        for idx, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                popidx = stack.pop()
                ans[popidx] = prices[popidx] - price
            
            stack.append(idx)
        return ans