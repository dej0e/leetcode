from enum import Enum
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preq[course].append(pre)
        
        cycle = set()
        completed = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in completed:
                return True

            cycle.add(course)
            for p in preq[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            completed.add(course)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True