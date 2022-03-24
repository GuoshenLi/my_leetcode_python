class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if abs(s_len - t_len) > 1:      #长度差距超过了1，不可能距离为1
            return False

        if s_len > t_len:               #为了好计算 前面的短，后面的长
            return self.isOneEditDistance(t, s)

        for i in range(s_len):
            if s[i] != t[i]:
                if s_len == t_len:      #长度一样，都跳过这一位
                    return s[i+1: ] == t[i+1: ]
                else:                   #短的不能跳，长的跳过这一位
                    return s[i: ] == t[i+1: ]

        return s_len + 1 == t_len       #for没比较来，只能是最后一位不同，或者完全相同

