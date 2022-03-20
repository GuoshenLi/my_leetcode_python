def add_two_number(l1, l2):


    carry = 0
    res = []
    while l1 and l2:
        digit1 = l1.pop()
        digit2 = l2.pop()
        digit = (digit1 + digit2 + carry) % 10
        carry = (digit1 + digit2 + carry) // 10

        res.append(digit)


    while l1:
        digit1 = l1.pop()
        digit = (digit1 + carry) % 10
        carry = (digit1 + carry) // 10
        res.append(digit)


    while l2:
        digit2 = l2.pop()
        digit = (digit2 + carry) % 10
        carry = (digit2 + carry) // 10
        res.append(digit)


    if carry:
        res.append(carry)

    return res[::-1]





if __name__ == '__main__':
    print(add_two_number(l1 = [2, 4, 3, 5, 6, 4, 7, 4],
                         l2 = [5, 6, 4, 4, 5, 6, 7]))



