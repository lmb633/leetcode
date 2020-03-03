class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        print(nums)
        result = []
        for idx1 in range(len(nums) - 3):
            num1 = nums[idx1]
            if idx1 > 0 and nums[idx1 - 1] == num1:
                continue
            print('i', idx1)
            for idx2 in range(idx1 + 1, len(nums) - 2):
                num2 = nums[idx2]
                if num2 > 0 and target - num1 < 0:
                    break
                if idx2 > idx1 + 1 and nums[idx2 - 1] == num2:
                    continue
                target0 = target - num1 - num2
                i = idx2 + 1
                j = len(nums) - 1
                while i < j :
                    temp = nums[i] + nums[j]
                    print(target0,idx1,idx2, i, j, temp)
                    if temp == target0:
                        result.append([num1, num2, nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < len(nums) and nums[i - 1] == nums[i]:
                            i += 1
                        while j > -1 and nums[j] == nums[j + 1]:
                            j -= 1
                    elif temp < target0:
                        i += 1
                        while i < len(nums) and nums[i - 1] == nums[i]:
                            i += 1
                    else:
                        j -= 1
                        while j > -1 and nums[j] == nums[j + 1]:
                            j -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [0,4,-5,2,-2,4,2,-1,4]
    print(solution.fourSum(nums, 12))
