class Solution(object):
    def calculate(self, s):
        stack = []
        result = []
        temp_num = -1
        s0 = self.split_str(s)
        # print(s0)
        for token in s0:
            if token == ' ':
                continue
            if token.isdigit():
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack:
                    t = stack.pop()
                    if t == '(':
                        break
                    else:
                        result.append(t)
            else:
                if not stack:
                    stack.append(token)
                else:
                    last = stack[-1]
                    if last == '(':
                        stack.append(token)
                    else:
                        result.append(stack.pop())
                        stack.append(token)
        while stack:
            result.append(stack.pop())
        stack = []
        for token in result:
            if token.isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b if token == '+' else a - b)
        return stack[-1]

    def split_str(self, tokens):
        tokens = tokens.replace(' ', "")
        i = 0
        j = 0
        result = []
        while j < len(tokens):
            if tokens[j].isdigit():
                j += 1
            else:
                if i == j:
                    result.append(tokens[i])
                else:
                    result.append(tokens[i:j])
                    result.append(tokens[j])
                j += 1
                i = j
        return result
