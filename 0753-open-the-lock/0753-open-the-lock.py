class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_children_neighbors(combination):
            res = []
            for i in range(4):
                digit = str((int(combination[i]) + 1) % 10)
                res.append(combination[:i] + digit + combination[i + 1:])
                digit2 = str((int(combination[i]) - 1 + 10) % 10)
                res.append(combination[:i] + digit2 + combination[i + 1:])
            return res

        queue = deque()
        queue.append(["0000", 0])
        visited = set(deadends)
        if "0000" in deadends:
            return -1
        while queue:
            combination, turns = queue.popleft()
            if combination == target:
                return turns
            for child in get_children_neighbors(combination):
                if child in visited:
                    continue
                visited.add(child)
                queue.append([child, turns + 1])

        return -1
