class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        print(nums)
        result = []
        for idx, num in enumerate(nums):
            if num > 0:
                break
            if idx > 0 and nums[idx - 1] == num:
                continue
            print('i', idx)
            target = 0 - num
            i = idx + 1
            j = len(nums) - 1
            while i < j and nums[j] >= 0:
                temp = nums[i] + nums[j]
                print(target, i, j, temp)
                if temp == target:
                    result.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i - 1] == nums[i]:
                        i += 1
                    while nums[j] == nums[j + 1]:
                        j -= 1
                elif temp < target:
                    i += 1
                    while nums[i - 1] == nums[i]:
                        i += 1
                else:
                    j -= 1
                    while nums[j] == nums[j + 1]:
                        j -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, 4]
    print(solution.threeSum(nums))
