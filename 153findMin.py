class Solution(object):
    def findMin(self, nums):
        def search(nums, low, high):
            if low == high:
                return nums[low]
            if low + 1 == high:
                return min(nums[low], nums[high])
            mid = (low + high) // 2
            if nums[mid] >= nums[low] and nums[mid] >= nums[high]:
                return search(nums, mid, high)
            else:
                return search(nums, low, mid)

        return search(nums, 0, len(nums) - 1)

        """
        :type nums: List[int]
        :rtype: int
        """
