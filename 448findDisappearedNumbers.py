class Solution(object):
    def findDisappearedNumbers(self, nums):
        result = []
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
