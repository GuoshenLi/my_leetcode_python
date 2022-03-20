class Solution:
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split('=')

        def parse(string):
            string = string.replace('-', '+-')
            if string[0] == '+': string = string[1:]

            string = string.split('+')
            count_x = 0
            num = 0

            for char in string:
                if char.endswith('x'):
                    tmp = char[:-1]
                    if tmp == '':
                        count_x += 1
                    elif tmp == '-':
                        count_x -= 1
                    else:
                        count_x += int(tmp)

                else:
                    num += int(char)

            return count_x, num


        lw, lb = parse(l)
        rw, rb = parse(r)
        fw = lw - rw
        fb = rb - lb
        if fw == 0:
            if fb == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        return 'x='+ str(fb // fw)

print(Solution().solveEquation(equation="x+5-3+x=6+x-2"))