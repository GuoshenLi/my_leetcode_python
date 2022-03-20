class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = [p for p in path.split('/') if p]
        # 执行完这一行语句只有三种字符，分别为 英文（文件名）/ '.'/ '..'
        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/' + '/'.join(stack)
