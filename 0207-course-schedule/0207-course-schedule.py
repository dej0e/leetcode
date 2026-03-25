from enum import Enum
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preq[course].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preq[course] == []:
                return True

            visited.add(course)
            for p in preq[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            preq[course] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True