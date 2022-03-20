import numpy as np
np.random.choice()
# 暴力递归 回溯 竟然过了
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        # 回溯
        length = len(num)

        def dfs(start, tmp):

            if start >= length:
                if len(tmp) < 3:
                    return None
                else:
                    if self.isvalid(tmp):
                        return True
                    return None

            for end in range(start, length):
                sub_num = num[start: end + 1]
                # 现在这里判断一下不会超时
                if len(sub_num) == len(str(int(sub_num))):
                    tmp.append(int(sub_num))
                    if dfs(end + 1, tmp):
                        return True
                    tmp.pop()
            return False

        return dfs(0, [])

    def isvalid(self, cum_list):
        i, j, k = 0, 1, 2
        length = len(cum_list)
        while k <= length - 1:
            if cum_list[i] + cum_list[j] != cum_list[k]:
                return False

            i += 1
            j += 1
            k += 1

        else:
            return True



# 递归 不是严格意义上的回溯 枚举所有可能的两个数 在剩下的字符串中找第三个数
class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        """
        | n1 | n2 | ....
        0    i    j
        两个分界点，分别用i和j来表示。

        :param num:
        :return:
        """

        def backtrack(n1, n2, r):
            """
            递归
            :param n1: 第一个数字。
            :param n2: 第二个数字。
            :param r: 剩下的数字。
            :return:
            """
            s = str(int(n1) + int(n2))
            if s == r:
                return True
            elif len(s) > len(r) or r[:len(s)] != s:
                return False
            else:
                return backtrack(n2, s, r[len(s):])

        def is_invalid_num(n):
            """
            判断是否为非法数字，以0开头，例如01,065
            :param n:
            :return:
            """
            return len(n) > 1 and n[0] == '0'

        for i in range(len(num)):  # 找到第一个数：num[:i]
            for j in range(i + 1, len(num)):  # 找到第二个数：num[i:j]
                num1, num2, rest = num[:i + 1], num[i + 1: j + 1], num[j + 1:]

                if is_invalid_num(num1) or is_invalid_num(num2):  # 避免0开头的非0数
                    continue
                if backtrack(num1, num2, rest):
                    return True
        return False
