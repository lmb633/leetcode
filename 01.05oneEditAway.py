class Solution(object):
    def oneEditAway(self, first, second):
        len1 = len(first)
        len2 = len(second)
        if abs(len1 - len2) > 1:
            return False
        if len1 == len2:
            diff = 0
            for i in range(len1):
                if first[i] != second[i]:
                    diff += 1
            if diff > 1:
                return False
            else:
                return True
        if len1 < len2:
            first, second = second, first
            len1, len2 = len2, len1
        i = 0
        j = 0
        while i < len1 and j < len2:
            if first[i] != second[j]:
                i += 1
            else:
                i += 1
                j += 1
        print(i, j)
        if i - j <= 1:
            return True
        else:
            return False

        """
        :type first: str
        :type second: str
        :rtype: bool
        """