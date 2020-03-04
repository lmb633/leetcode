import sys


class Solution(object):
    def minWindow(self, s, t):
        strlist = self.get_set(t)
        i = 0
        j = 0
        lens = len(s)
        lent = len(t)
        minlength = sys.maxsize
        result = (0, sys.maxsize)
        while i < lens and s[i] not in t:
            i += 1
            j += 1
        while j < lens and i <= lens - lent:
            while not self.check(strlist)and j<lens:
                if s[j] in t:
                    strlist[s[j]] = strlist[s[j]] - 1
                j += 1
            # print('i,j', i, j)
            while self.check(strlist):
                if minlength > j - i:
                    minlength = j - i
                    result = (i, j)
                if s[i] in t:
                    strlist[s[i]] = strlist[s[i]] + 1
                i += 1
        return s[result[0]:result[1]] if result != (0, sys.maxsize) else ''

    def get_set(self, list):
        str_set = {}
        for s in list:
            if s in str_set:
                str_set[s] = str_set[s] + 1
            else:
                str_set[s] = 1
        return str_set

    def check(self, strlist):
        for v in strlist.values():
            if v > 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "aaa"
    t = "aaa"
    print(solution.minWindow(s, t))
