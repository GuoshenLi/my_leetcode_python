class Solution:
    def reverse(self, x: int) -> int:

        reverse_x = 0
        sig = x
        x = abs(x)

        while True:
            reverse_x = 10 * reverse_x + x % 10
            x = x // 10

            if reverse_x > 2 ** 31:
                return 0

            elif x == 0:
                if sig > 0:
                    return reverse_x
                else:
                    return - reverse_x



