class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures) 
        stack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                answer[stackIndex] = i - stackIndex
            stack.append((temperatures[i], i))
        return answer