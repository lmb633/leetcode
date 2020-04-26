class Solution(object):
    def partition(self, s):
        result = []

        def is_p(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(prefix, left, result):
            # print(prefix,left,result)
            if left == '':
                result.append(prefix)
                return
            for i in range(1, len(left) + 1):
                if is_p(left[0:i]):
                    helper(prefix + [left[0:i]], left[i:], result)

        helper([], s, result)
        return result

        """
        :type s: str
        :rtype: List[List[str]]
        """
