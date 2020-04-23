class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        self.process([], target, candidates, result)
        return result

    def process(self, prefix, target, left, result):
        # print('process', prefix, target, left, result)
        remove = []
        left_set = set(left)
        for num in left_set:
            if len(prefix) == 0 or num >= prefix[-1]:
                if num == target:
                    result.append(prefix + [num])
                elif num > target:
                    remove.append(num)
                else:
                    temp = [n for n in left]
                    for r in remove:
                        temp.remove(r)
                    temp.remove(num)
                    self.process(prefix + [num], target - num, temp, result)
