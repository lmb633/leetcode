class Solution(object):
    def rob(self, nums):

        def helper(nums):
            if not nums:
                return 0
            length = len(nums)
            result = [0] * (length + 1)
            result[1] = nums[0]
            for i in range(2, length + 1):
                result[i] = max(result[i - 1], result[i - 2] + nums[i - 1])
            return result[-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
        """
        :type nums: List[int]
        :rtype: int
        """
