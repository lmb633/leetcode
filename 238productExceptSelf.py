class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [1] * length
        right = [1] * length
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i]
            right[length - 1 - i] = right[length - i] * nums[length - 1 - i]
        result = [1] * length
        result[0] = right[1]
        result[-1] = left[-2]
        for i in range(1, length - 1):
            result[i] = left[i - 1] * right[i + 1]
        return result
