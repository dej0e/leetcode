class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low < high:
            hours_spent = 0
            k = (low + high) // 2
            for pile in piles:
                hours_spent += math.ceil(pile/k)
            if hours_spent <= h:
                res = k
                high = k
            else:
                low = k + 1 
        return res