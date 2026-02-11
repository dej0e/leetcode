from enum import Enum
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for course, prereq in prerequisites:
            premap[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False  # cycle
            if premap[course] == []:  # no more prereqs
                return True

            visiting.add(course)
            for prereq in premap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            premap[course] = []  # all prereqs are counted already
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
