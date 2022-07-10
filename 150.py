class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f1 = lambda a , b : a + b
        f2 = lambda a , b : a - b
        f3 = lambda a , b : a * b
        f4 = lambda a , b : int(a / b)

        match_dict = {'+' : f1, '-': f2, '*' : f3, '/': f4}
        stack = []
        for character in tokens:
            if character in match_dict:
                a = stack.pop()
                b = stack.pop()
                stack.append(match_dict[character](b, a))

            else:
                stack.append(int(character))

        return stack[0]




class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for item in tokens:
            if item == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) + int(b))

            elif item == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))

            elif item == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) * int(b))

            elif item == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) / int(a))

            else:
                stack.append(item)

        return int(stack[0])
