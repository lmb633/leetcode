class Solution(object):
    def findContinuousSequence(self, target):
        length = target // 2 + 1
        print(length)
        i = 1
        j = 1
        result = []
        temp_sum = 0
        while i <= j and j <= length:
            while j <= length and temp_sum < target:
                temp_sum += j
                j += 1
            if temp_sum == target:
                result.append([num for num in range(i, j)])
                temp_sum -= i
                i += 1
            # print(i, j, temp_sum)
            while i < j and temp_sum > target:
                temp_sum -= i
                i += 1
            if temp_sum == target:
                result.append([num for num in range(i, j)])
                temp_sum -= i
                i += 1
            # print(i, j, temp_sum)
        return result


solution = Solution()
print(solution.findContinuousSequence(9))
