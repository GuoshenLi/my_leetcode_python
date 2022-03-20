from collections import deque, defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for word in words:
            for char in word:
                in_degree[char] = 0

        for i in range(len(words) - 1):
            cur_word = words[i]
            next_word= words[i + 1]

            if len(cur_word) > len(next_word) and cur_word.find(next_word) == 0:
                return ''

            min_length = min(len(cur_word), len(next_word))
            for j in range(min_length):
                if cur_word[j] != next_word[j]:
                    graph[cur_word[j]].append(next_word[j])
                    in_degree[next_word[j]] += 1
                    break

        res = []

        queue = deque()
        for char, degree in in_degree.items():
            if degree == 0:
                queue.append(char)

        while queue:
            node = queue.popleft()
            res.append(node)

            for next_node in graph[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        if len(res) == len(in_degree):
            return ''.join(res)
        else:
            return ''