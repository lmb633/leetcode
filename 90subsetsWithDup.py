class Solution(object):
    def subsetsWithDup(self, nums):
        nums_set = {}
        for num in nums:
            if num not in nums_set:
                nums_set[num] = 1
            else:
                nums_set[num] = nums_set[num] + 1
        result = [[]]
        print(nums_set)
        for num in nums_set:
            temp = []
            temp_result = []
            for i in range(nums_set[num]):
                temp.append([num] * (i + 1))
            print(temp)
            for subset in result:
                for x in temp:
                    temp_result.append(subset + x)
                temp_result.append(subset)
            result = temp_result
            print(result)
        return result


nums = [1, 2, 2]
solution = Solution()
print(solution.subsetsWithDup(nums))
