class Solution(object):
    def numberOfSubstrings(self, s):
        cur_set = {'a': 0, 'b': 0, 'c': 0}

        def check(cur):
            for k in cur:
                if cur[k] <= 0:
                    return False
            return True

        i = j = 0
        result = 0
        length = len(s)
        while j < length and i < length:
            while j < length and not check(cur_set):
                cur_set[s[j]] = cur_set[s[j]] + 1
                j += 1
            if check(cur_set):
                result += length - j + 1
            while True:
                cur_set[s[i]] = cur_set[s[i]] - 1
                i += 1
                if check(cur_set):
                    result += length - j + 1
                else:
                    break
                    # print(i,j,result)
        return result

        """
        :type s: str
        :rtype: int
        """
