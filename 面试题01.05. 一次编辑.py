
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:] or first[i:] == second[i + 1:]  # 注：改用下标枚举可达到 O(1) 空间复杂度
                #      对应改                                          对应删除一个 从first 到 second                 对应增加一个

        return True
