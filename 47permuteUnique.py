class Solution(object):
    def permute(self, nums):
        result = []
        self.process([], nums, result)
        return result

    def process(self, prefex, left, result):
        print(left)
        if len(left) <= 1:
            result.append(prefex + left)
            # print(result)
            return
        else:
            nums_set = set(left)
            for num in nums_set:
                temp = [num for num in left]
                temp.remove(num)
                temp2 = [num for num in prefex]
                temp2.append(num)
                self.process(temp2, temp, result)


nums = [1, 1, 2]
print(set(nums))
solution = Solution()
print(solution.permute(nums))
