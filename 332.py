from collections import defaultdict
# 加个visited数组好理解很多
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        path = ['JFK']
        id_map = defaultdict(list)
        visited = defaultdict(list)

        # key: 出发地，val: 到达地
        for ticket in tickets:
            id_map[ticket[0]].append(ticket[1])
            visited[ticket[0]].append(False)

        m = len(tickets)

        for k, v in id_map.items():
            id_map[k].sort()

        def dfs(depart_city):
            if len(path) == m + 1:
                return True
            if depart_city not in id_map:
                return False


            for i in range(len(id_map[depart_city])):
                if visited[depart_city][i] == False:
                    visited[depart_city][i] = True
                    next_city = id_map[depart_city][i]
                    path.append(next_city)

                    if dfs(next_city):
                        return True

                    visited[depart_city][i] = False
                    path.pop()



        dfs('JFK')

        return path