class Solution:
    def checkValidString(self, s):
        stack_left = []
        stack_star = []

        for i in range(len(s)):
            if s[i] == '(':
                stack_left.append(i)
            elif s[i] == '*':
                stack_star.append(i)
            else:
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        # 有可能出现 '*('   这个要不断尝试的。。。
        # 要判断这个就比较难了
        #
        while stack_left and stack_star:
            if stack_left[-1] > stack_star[-1]:
                return False
            stack_left.pop()
            stack_star.pop()
        # 判断stack_left 是否为空即可
        # 因为stack_star 中 star可以为任何东西 因此不用管
        return len(stack_left) == 0
