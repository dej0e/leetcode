from enum import Enum


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle = set()
        visited = set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            prereq[crs] = []
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res if len(visited) == numCourses else []