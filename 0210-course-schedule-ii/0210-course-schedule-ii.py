from enum import Enum


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for course, pr in prerequisites:
            prereq[course].append(pr)
        
        res = []
        completed = set()
        cycle = set()
        def dfs(course):
            if course in cycle:
                return False
            
            if course in completed:
                return True
            
            
            cycle.add(course)
            for p in prereq[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            completed.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


        