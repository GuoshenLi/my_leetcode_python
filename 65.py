class Solution:
    def isNumber(self, s: str) -> bool:
        # 统计s中有多少个. 或者e / E

        point = -1
        e = -1
        for i in range(len(s)):
            if s[i] == '.':
                if point == -1:
                    point = i
                else:
                    return False

            if s[i] == 'e' or s[i] == 'E':
                if e == -1:
                    e = i
                else:
                    return False

        # full integer 没有点 也没有e
        if point == -1 and e == -1:
            return self.isinteger(s)

        # decimal + E/e + integer
        if point != -1 and e != -1:
            if e < point: return False

            return self.isdecimal(s[0:e]) and self.isinteger(s[e + 1:])

        # full decimal 有. 没有e
        if point != -1 and e == -1:
            return self.isdecimal(s)

        # 没有. 有e
        if point == -1 and e != -1:
            # integer + E/e + integer
            return self.isinteger(s[0: e]) and self.isinteger(s[e + 1:])

    def isinteger(self, s: str) -> bool:
        if len(s) < 1: return False
        if len(s) == 1: return s[0].isdigit()
        if not s[0].isdigit():
            if s[0] != '+' and s[0] != '-':
                return False

        for i in range(1, len(s)):
            if not s[i].isdigit():
                return False

        return True

    def isdecimal(self, s: str) -> bool:
        if len(s) < 2: return False
        count = 0
        if not s[0].isdigit():
            if s[0] != '+' and s[0] != '-' and s[0] != '.':
                return False

        else:
            count += 1

        for i in range(1, len(s)):
            if s[i].isdigit():
                count += 1

            else:
                if s[i] != '.':
                    return False

        return count > 0
