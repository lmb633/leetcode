class Solution(object):
    def maxSubArray(self, nums):
        temp_max = 0
        max_ = -2 ** 32
        for i in range(len(nums)):
            temp_max += nums[i]
            if temp_max > max_:
                max_ = temp_max
            if temp_max < 0:
                temp_max = 0
        return max_
