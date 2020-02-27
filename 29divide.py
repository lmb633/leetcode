class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        flag = 1
        if dividend ^ divisor < 0:
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += (1 << i)
                dividend -= divisor << i
        return result if flag > 0 else -result

