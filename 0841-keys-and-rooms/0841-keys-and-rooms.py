class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = {i:[] for i in range(len(rooms))}
        for room, keys in enumerate(rooms):
            for key in keys:
                adj[room].append(key)
        


        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            room = q.popleft()
            for room_accessible in adj[room]:
                if room_accessible in visited:
                    continue
                q.append(room_accessible)
                visited.add(room_accessible)
        return len(visited) == len(rooms)
