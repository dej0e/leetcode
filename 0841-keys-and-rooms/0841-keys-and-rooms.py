class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        def dfs(room):
            if room in visited:
                return
            
            visited.add(room)
            for room_accessible in rooms[room]:
                dfs(room_accessible)
        
        dfs(0)
        return len(visited) == len(rooms)

        # q = deque()
        # q.append(0)
        # visited = set()
        # visited.add(0)

        # while q:
        #     room = q.popleft()
        #     for room_accessible in adj[room]:
        #         if room_accessible in visited:
        #             continue
        #         q.append(room_accessible)
        #         visited.add(room_accessible)
        # return len(visited) == len(rooms)
