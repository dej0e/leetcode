from enum import Enum


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class State(Enum):
            NOT_VISITED = 0
            VISITED = 1
            VISITING = 2

        graph = {}
        states = {}
        for node in range(numCourses):
            graph[node] = []
            states[node] = State.NOT_VISITED

        for subject, prereq in prerequisites:
            graph[subject].append(prereq)

        path = []

        def dfs(start):
            #Cycle in Graph
            if states[start] == State.VISITING:
                return False
            #Already completed prerequisite
            if states[start] == State.VISITED:
                return True

            states[start] = State.VISITING
            for prereq in graph[start]:
                if not dfs(prereq):
                    return False
            states[start] = State.VISITED
            path.append(start)
            return True

        for i in range(numCourses):
            if states[i] == State.NOT_VISITED and not dfs(i):
                return []
        return path
