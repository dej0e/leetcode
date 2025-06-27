from enum import Enum


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class State(Enum):
            TO_VISIT = 0
            VISITING = 1
            VISITED = 2

        graph = {node: [] for node in range(numCourses)}
        states = [State.TO_VISIT for node in range(numCourses)]
        for src, dest in prerequisites:
            graph[src].append(dest)

        def dfs(start):
            states[start] = State.VISITING
            for next_vertex in graph[start]:
                if states[next_vertex] == State.VISITED:
                    continue
                if states[next_vertex] == State.VISITING:
                    return False
                if not dfs(next_vertex):
                    return False
            states[start] = State.VISITED
            return True

        return all(dfs(i) for i in range(numCourses))
