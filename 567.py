# 枚举s1所有排列 判断在不在s2当中
# 严重超时

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_list = list(s1)
        length = len(s1_list)
        visited = [False] * len(s1_list)

        def dfs(level, tmp):
            if level == length:
                if ''.join(tmp) in s2:
                    return True

            for i in range(length):
                if visited[i] is False:
                    visited[i] = True
                    tmp.append(s1_list[i])
                    if dfs(level + 1, tmp):
                        return True
                    tmp.pop()
                    visited[i] = False

            return False

        return dfs(0, [])

# 其实是一个典型的滑动窗口 和题目438 其实都一样
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_array = [0] * 26
        window_array = [0] * 26

        length_s1 = len(s1)
        length_s2 = len(s2)

        if length_s2 < length_s1:
            return False

        for i in range(length_s1):
            s1_array[ord(s1[i]) - ord('a')] += 1
            window_array[ord(s2[i]) - ord('a')] += 1
        if s1_array == window_array:
            return True

        for i in range(length_s1, length_s2):
            window_array[ord(s2[i - length_s1]) - ord('a')] -= 1
            window_array[ord(s2[i]) - ord('a')] += 1
            if s1_array == window_array:
                return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        diff_array = [0] * 26

        for i in range(len(s1)):
            diff_array[ord(s2[i]) - ord("a")] += 1
            diff_array[ord(s1[i]) - ord("a")] -= 1

        diff_count = [item != 0 for item in diff_array].count(True)

        if diff_count == 0: return True

        for i in range(len(s1), len(s2)):
            if diff_array[ord(s2[i]) - ord("a")] == -1:
                diff_count -= 1
            elif diff_array[ord(s2[i]) - ord("a")] == 0:
                diff_count += 1

            diff_array[ord(s2[i]) - ord("a")] += 1

            if diff_array[ord(s2[i - len(s1)]) - ord("a")] == 1:
                diff_count -= 1
            elif diff_array[ord(s2[i - len(s1)]) - ord("a")] == 0:
                diff_count += 1

            diff_array[ord(s2[i - len(s1)]) - ord("a")] -= 1

            if diff_count == 0:
                return True

        return False


print(Solution().checkInclusion(s1 = "ab" , s2 = "eidbaooo"))