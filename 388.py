# 栈 单调栈
class Solution:
    def lengthLongestPath(self, input: str) -> int:

        def cal_len(stack):
            ans = 0
            for s in stack:
                ans += len(s[1])
            # 多加 len(stack) - 1 个 "/"
            return ans + len(stack) - 1

        s = input.split("\n")

        # 记录缩进个数和字符串
        t = []
        for a in s:
            num = a.count("\t")
            t.append([num, a[num:]])

        stack = []
        res = 0
        for a in t:
            # 总是保证栈顶是小于该文件的缩进的 严格的单调递增栈
            while stack and stack[-1][0] >= a[0]:
                stack.pop()
            stack.append(a)
            if "." in a[1]:
                # print(stack)
                res = max(res, cal_len(stack))

        return res

print(Solution().lengthLongestPath(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))