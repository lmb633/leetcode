def get_rpn(tokens):
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    result = []
    for token in tokens:
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
        elif token in op:
            if not stack:
                stack.append(token)
            else:
                while stack:
                    last = stack[-1]
                    if op[last] < op[token]:
                        break
                    else:
                        result.append(stack.pop())
                stack.append(token)
        print('result', result)
        print('stack', stack)
    while stack:
        result.append(stack.pop())
    return result


tokens = '(1+2)*(3+4)'
# tokens = '(1+2*(4-3)+6/2)'
print(get_rpn(tokens))
