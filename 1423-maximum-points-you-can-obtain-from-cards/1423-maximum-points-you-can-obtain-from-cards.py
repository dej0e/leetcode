class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        leftsum = rightsum = maxsum = 0
        for i in range(0, k):
            leftsum = leftsum + cardPoints[i]
        maxsum = leftsum
        right_index = len(cardPoints) - 1
        for i in range(k-1, -1, -1):
            leftsum = leftsum - cardPoints[i]
            rightsum = rightsum + cardPoints[right_index]
            right_index -= 1
            maxsum = max(maxsum, leftsum + rightsum)
        return maxsum