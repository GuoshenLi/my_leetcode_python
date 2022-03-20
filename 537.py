class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # (a + b * i) * (x + y * i) = ax - by + i * (ay + bx)
        a_t, a_f = int(a.split('+')[0]), int(a.split('+')[1].split('i')[0])
        b_t, b_f = int(b.split('+')[0]), int(b.split('+')[1].split('i')[0])
        res_t, res_f = a_t * b_t - a_f * b_f, a_t * b_f + a_f * b_t
        return str(res_t) + "+" + str(res_f) + "i"