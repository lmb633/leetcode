class Solution(object):
    def decodeString(self, s):
        if s is None or s == '':
            return s
        i = 0
        result = ''
        while i < len(s) and s[i].isalpha():
            result += s[i]
            i += 1
        if i >= len(s):
            return result
        times = 0
        while s[i].isdigit():
            times = times * 10 + int(s[i])
            i += 1
        i += 1
        temp_str = ''
        while i < len(s):
            if s[i] == ']':
                break
            elif s[i].isalpha():
                temp_str += s[i]
                i += 1
            elif s[i].isdigit():
                j = i + 1
                while s[j].isdigit():
                    j += 1
                j += 1
                stack = ['[']
                while stack:
                    if s[j] == '[':
                        stack.append('[')
                    elif s[j] == ']':
                        stack.pop()
                    j += 1
                temp_str += self.decodeString(s[i:j])
                i = j
        result = result + temp_str * times
        return result + self.decodeString(s[i + 1:])