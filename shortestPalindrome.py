class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s

        def get_next(s):
            length = len(s)
            next_array = [0] * length
            next_array[0] = -1
            i = 0
            j = 1
            while j < length - 1:
                if i == -1 or s[i] == s[j]:
                    next_array[j + 1] = i + 1
                    i += 1
                    j += 1
                else:
                    i = next_array[i]
            return next_array

        next_array = get_next(s)
        # print(next_array)
        reverse_s = s[::-1]
        i = 0
        j = 0
        length = len(s)
        while i < length and j < length:
            if j == -1 or reverse_s[i] == s[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]
        # print(j)
        return reverse_s + s[j:]

        """
        :type s: str
        :rtype: str
        """
