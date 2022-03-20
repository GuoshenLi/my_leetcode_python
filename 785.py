# 判断二分图 染色法 bfs


from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # visited 0, 1, -1 未访问，+ 两种颜色
        visited = [0 for i in range(len(graph))]

        for i in range(len(graph)):
            if visited[i] != 0: continue
            # 去check每一个cc (连通域)
            queue = deque()
            queue.append(i)
            visited[i] = 1

            while queue:
                node = queue.popleft()
                for next_node in graph[node]:
                    if visited[next_node] == visited[node]:
                        return False

                    if visited[next_node] == 0:
                        visited[next_node] = -visited[node]
                        queue.append(next_node)


        return True





class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        states = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if states[i] == 0 and not self.check_valid_color(graph, i, 1, states):
                # 去check每一个cc (连通域)
                return False

        return True


    def check_valid_color(self, graph, node, need_color, states):
        if states[node] != 0:
            return states[node] == need_color

        states[node] = need_color

        for next_node in graph[node]:
            if not self.check_valid_color(graph, next_node,     -need_color, states):
                return False

        return True



