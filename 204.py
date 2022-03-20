# 厄拉多塞筛法
# 非常牛逼 如果是None 就划去其倍数
# 比如说求20以内质数的个数,首先0,1不是质数.
# 2是第一个质数,然后把20以内所有2的倍数划去.
# 2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.
# 3后面紧跟的数即为下一个质数5,再把5所有的倍数划去.
# 以此类推.



class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        flag = [None] * n
        flag[0] = False
        flag[1] = False
        for i in range(2, n):
            if flag[i] == None:
                flag[i] = True

                for j in range(i * i, n, i):
                    flag[j] = False

        return sum(flag)


# 暴力搜索 超时
class Solution:
    def countPrimes(self, n: int) -> int:

        def isprime(num):
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

        count = 0

        for i in range(2, n):
            if isprime(i):
                count += 1

        return count