from collections import deque


class Solution:
    def sequenceReconstruction(
        self, nums: List[int], sequences: List[List[int]]
    ) -> bool:
        def find_indegree(graph):
            indegree = {node: 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        def topo_sort(graph):
            seq = []
            q = deque()
            indegree = find_indegree(graph)
            for node in graph:
                if indegree[node] == 0:
                    q.append(node)
            while len(q) > 0:
                if len(q) > 1:
                    return False
                node = q.popleft()
                seq.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return seq == nums

        n = len(nums)
        graph: dict(int, set(int)) = {node: set() for node in range(1, 1 + n)}
        for seq in sequences:
            for i in range(len(seq) - 1):
                source, destination = seq[i], seq[i + 1]
                graph[source].add(destination)
        return topo_sort(graph)
