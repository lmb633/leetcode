class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ''
        result = ''
        i = 0
        flag = True
        while flag:
            print(result)
            if len(strs[0]) > i:
                result = result + strs[0][i]
            else:
                result = result + ' '
                break
            for s in strs:
                if len(s) < i + 1 or s[i] != result[i]:
                    flag = False
                    break
            i += 1
        return result[:-1]


class Solution2(object):
    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ''
        result = strs[0]
        for s in strs[1:]:
            result = self.prefix(result, s)
            print(result)
            if result == '':
                break
        return result

    def prefix(self, s1, s2):
        length = min(len(s1), len(s2))
        i = 0
        for i in range(length):
            if s1[i] == s2[i]:
                i += 1
            else:
                break
        result = s1[:i]
        return result


solution = Solution2()
strs = ["aa", "a"]
print(solution.longestCommonPrefix(strs))
