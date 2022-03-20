class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        count = 0
        for i in range(32):
            if y & 1 != x & 1:
                count += 1
            x = x >> 1
            y = y >> 1

        return count