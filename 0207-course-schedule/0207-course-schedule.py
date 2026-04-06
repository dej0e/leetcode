from enum import Enum
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # premap = defaultdict(list)
        # for crs, pre in prerequisites:
        #     premap[crs].append(pre)
        
        # visiting = set()
        # def dfs(crs):
        #     if crs in visiting:
        #         return False
            
        #     if premap[crs] == []:
        #         return True
            
        #     visiting.add(crs)
        #     for pre in premap[crs]:
        #         if not dfs(pre):
        #             return False
            
        #     visiting.remove(crs)
        #     premap[crs] = []
        #     return True

            
        
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        
        # return True

        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True