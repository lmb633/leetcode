class Solution(object):
    def romanToInt(self, s):
        trans_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0
        i = 0
        while i < len(s):
            temp = trans_map[s[i]]
            i += 1
            if i < len(s):
                if s[i - 1:i + 1] in trans_map:
                    temp = trans_map[s[i - 1:i + 1]]
                    i += 1
            result += temp
        return result
        """
        :type s: str
        :rtype: int
        """
