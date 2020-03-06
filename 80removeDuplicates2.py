class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        sum_ = 1

        flag = True
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i + 1]
                j += 1
                sum_ += 1

                flag = True
            elif nums[i] == nums[i + 1] and flag:
                nums[j] = nums[i + 1]
                j += 1
                sum_ += 1
                flag = False
            print(i,j,flag,sum_)
        return sum_


nums = [1, 1, 1,  2, 2, 3]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
