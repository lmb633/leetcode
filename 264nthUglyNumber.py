# 超时
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i = 1
        while n > 0:
            if self.check(i):
                n -= 1
                if n == 0:
                    return i
                i += 1
            else:
                i += 1

    def check(self, n):
        if n == 1:
            return True
        while n >= 2:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                break
        if n == 1:
            return True
        else:
            return False


import heapq


class Solution2:
    def nthUglyNumber(self, n):
        nums = []
        result = []
        result_set = set()
        result.append(1)
        result_set.add(1)
        i = 0
        while i < n:
            temp = heapq.heappop(result)
            nums.append(temp)
            temp = [temp * 2, temp * 3, temp * 5]
            for t in temp:
                if t not in result_set:
                    result_set.add(t)
                    heapq.heappush(result, t)
            i += 1
        return nums[-1]


class Solution3:
    def nthUglyNumber(self, n):
        result = []
        result.append(1)
        i, j, k = 0, 0, 0
        while len(result) < n:
            a = result[i] * 2
            b = result[j] * 3
            c = result[k] * 5
            min_ = min(a, b, c)
            if min_ != result[-1]:
                result.append(min_)
            if min_ == a:
                i += 1
            elif min_ == b:
                j += 1
            else:
                k += 1
        # print(result)
        return result[-1]
