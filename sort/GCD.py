

def GCD(a, b):
    if b == 0: return a
    return GCD(b, a % b)

def GCD_2(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(GCD_2(12000, 16))
