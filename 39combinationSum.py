class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.process([], target, candidates, result)
        return result

    def process(self, prefix, target, left, result):
        print('process', prefix, target, left, result)
        remove = []
        for num in left:
            if len(prefix) == 0 or num >= prefix[-1]:

                if num == target:
                    result.append(prefix + [num])
                elif num > target:
                    remove.append(num)
                else:
                    temp = [num for num in left]
                    for r in remove:
                        temp.remove(r)
                    self.process(prefix + [num], target - num, temp, result)
        print(result)


nums = [8, 7, 4,3]
target = 11
solution = Solution()
print('result', solution.combinationSum(nums, target))
# solution.process([4], 7, [8,7, 4], [])
