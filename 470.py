# 微信面试 字节跳动面试
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 文章基于这样一个事实 (randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数

# 若rand10生成 rand7可以直接拒绝采样
# 若rand4生成rand2（成倍数）可以直接拒绝采样，更方便的方法是可以rand4 % # 2 + 1
# rand4  % 2 + 1
# 1  %  2 + 1 = 2
# 2  %  2 + 1 = 1
# 3  %  2 + 1 = 2
# 4  %  2 + 1 = 1
# 刚好等于rand2 牛逼牛逼

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7() # rand49
            if num <= 40:
                return num % 10 + 1


