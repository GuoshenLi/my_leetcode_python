from typing import List


class Solution:
    def removeComments(self, source):
        inBlock = False
        res = []

        for line in source:

            i = 0
            if not inBlock:
                tmp = []
            while i < len(line):
                if line[i:i + 2] == "/*" and not inBlock:
                    inBlock = True
                    i += 1

                elif line[i:i + 2] == "*/" and inBlock:
                    inBlock = False
                    i += 1

                elif line[i: i + 2] == "//" and not inBlock:
                    break

                elif not inBlock:
                    tmp.append(line[i])

                i += 1
            if not inBlock and tmp:
                res.append("".join(tmp))


        return res


print(Solution().removeComments(source = ["a/*comment", "line", "more_comment*/b"]))