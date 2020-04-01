class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        length = len(s)
        result = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                temp = ''
                j = i
                while j < length:
                    temp += s[j]
                    j += 2 * numRows - 2
                result += temp

            else:
                temp = ''
                j = i
                while j < length:
                    temp += s[j]
                    j1 = j + 2 * numRows - i * 2 - 2
                    if j1 < length:
                        temp += s[j1]
                    j += numRows * 2 - 2
                result += temp
        return result

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """