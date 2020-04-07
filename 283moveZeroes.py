class Solution(object):
    def moveZeroes(self, nums):
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
