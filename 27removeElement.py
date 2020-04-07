class Solution(object):
    def removeElement(self, nums, val):
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
