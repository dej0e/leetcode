class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        cars = [] 
        while i < len(position):
            cars.append((position[i], speed[i]))
            i += 1
        
        stack = []
        cars.sort(key=lambda x: x[0])
        for pos, s in cars[::-1]:
            time = (target - pos) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)