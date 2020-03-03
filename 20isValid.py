class Solution(object):
    def isValid(self, s):
        a = list()
        for s0 in s:
            if s0 in ['[', '{', '(']:
                a.append(s0)
            else:
                if len(a) == 0:
                    return False
                s1 = a.pop()
                if not (s1 == '[' and s0 == ']' or s1 == '{' and s0 == '}' or s1 == '(' and s0 == ')'):
                    return False
        return True if len(a) == 0 else False


if __name__ == '__main__':
    solution = Solution()
    s = '{[}}'
    print(solution.isValid(s))
