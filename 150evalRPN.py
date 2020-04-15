class Solution(object):
    def evalRPN(self, tokens):
        def calculate(a, b, op):
            a = int(a)
            b = int(b)
            print(a, b, op)
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return abs(a) // abs(b) if a * b >= 0 else -(abs(a) // abs(b))
        stack0 = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack0.append(token)
            else:
                b = stack0.pop()
                a = stack0.pop()
                stack0.append(calculate(a, b, token))
                # print(stack0)
        return int(stack0[-1])
