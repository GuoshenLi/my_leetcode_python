# bfs
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = deque()
        queue.append(0)
        n = len(rooms)
        visited = [False for i in range(n)]
        visited[0] = True

        while queue:
            node = queue.popleft()
            for next_node in rooms[node]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True

        return all(visited)



class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        can_reach = [False] * n

        @lru_cache(None)
        def dfs(index):
            visited[index] = True
            can_reach[index] = True
            for next_index in rooms[index]:
                if not visited[next_index] and dfs(next_index):
                    return True
            visited[index] = False
            return False


        dfs(0)
        return all(can_reach)



class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room_index):
            visited.add(room_index)
            for key in rooms[room_index]:
                if key not in visited:
                    dfs(key)
        dfs(0)

        return len(visited) == len(rooms)

