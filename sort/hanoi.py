# n个盘子从a经过b移动到c
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("moving from {} to {}".format(a, c))
        hanoi(n - 1, b, a, c)


hanoi(2, 'a', 'b', 'c')
