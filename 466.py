# 暴力解法 双指针 明显超时
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        index2 = 0
        count = 0
        length_1 = len(s1)
        length_2 = len(s2)

        for i in range(n1):
            for index1 in range(length_1):

                if s1[index1] == s2[index2]:
                    index2 += 1

                if index2 == length_2:
                    count += 1
                    index2 = 0

        return count // n2




# 思路：
# dp[i][0]：s2的第i个字符开始与s1的第1个字符比较，记录单次在s1的长度比较下，s2完整比较的次数
# dp[i][1]：s2的第i个字符开始与s1的第1个字符比较，记录单次在s1的长度比较下，下一轮开始比较的s2的字符位置
#
# s1在n1次长度中出现s2的次数sum的计算方式：
# begin = 0,sum = 0;
# for(int i = 0 ; i < n1; i++){
#     sum += dp[begin][0];
#     begin = dp[begin][1];
# }
#
# n1个s1出现n2个s2的次数为：sum/s2;



class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        res = 0

        length_s1 = len(s1)
        length_s2 = len(s2)
        dp = [[0, 0] for i in range(length_s2)]

        for i in range(length_s2):
            begin = i
            tmpRes = 0
            for j in range(length_s1):
                if s1[j] == s2[begin]:
                    begin += 1
                    # s2的begin遍历是可以循环的
                if begin == length_s2:
                    begin = 0
                    tmpRes += 1

            dp[i][0] = tmpRes
            dp[i][1] = begin

        begin = 0
        for i in range(n1):
            res += dp[begin][0]
            begin = dp[begin][1]


        return res // n2


print(Solution().getMaxRepetitions(s1 = "abaacdbac", n1 = 4, s2 = "adcbd", n2 = 1))