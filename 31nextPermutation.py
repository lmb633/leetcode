class Solution(object):
    def nextPermutation(self, nums):
        if not nums:
            return nums
        length = len(nums)
        i = length - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        i = i - 1
        if i >= 0:
            j = length - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j = length - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
