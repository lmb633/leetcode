class Solution(object):
    def subsets(self, nums):
        if not nums:
            return [[]]
        num = nums[0]
        subsets = self.subsets(nums[1:])
        result = []
        for sub in subsets:
            result.append([num] + sub)
            result.append(sub)
        print(result)
        return result


class Solution2(object):
    def subsets(self, nums):
        result = []
        result.append([])
        for num in nums:
            temp = []
            for sub in result:
                temp.append(sub + [num])
                temp.append(sub)
            result = temp
        return result


nums = [1, 2, 3]
solution = Solution2()
print(solution.subsets(nums))
