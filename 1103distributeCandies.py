class Solution(object):
    def distributeCandies(self, candies, num_people):
        left = candies
        i = 0
        # 这一步也可以用一个不等式来求解
        while left >= 0:
            i += 1
            left -= ((2 * i - 1) * num_people + 1) * num_people / 2
        times = i - 1
        print(times)
        result = [0] * num_people
        if times > 0:
            for i in range(num_people):
                result[i] = int((times ** 2 - times) * num_people / 2 + times * (i + 1))
        # print(result)
        left = candies - sum(result)
        i = 0
        while left > 0:
            result[i] += min(times * num_people + i + 1, left)
            left -= (times * num_people + i + 1)
            i += 1
            # print(result, left)
        return result


solution = Solution()
print(solution.distributeCandies(80, 4))
