class Solution(object):
    def isValid(self, s):
        stack = list()
        for s0 in s:
            stack.append(s0)
            if len(stack) > 2:
                if stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                    stack.pop()
                    stack.pop()
                    stack.pop()
            else:
                if len(stack) == 2:
                    if not (stack[0] == 'a' and (stack[1] == 'b' or stack[1] == 'a')):
                        return False
                if len(stack) == 1:
                    if not stack[0] == 'a':
                        return False
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    solution = Solution()
    s = 'cababc'
    print(solution.isValid(s))
