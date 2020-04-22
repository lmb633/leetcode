class Solution(object):
    def search(self, nums, target):
        def helper(nums, low, high, target):
            if low > high:
                return False
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            while low + 1 <= high and nums[low] == nums[low + 1]:
                low += 1
            while high - 1 >= low and nums[high] == nums[high - 1]:
                high -= 1
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[low]:
                if nums[mid] > target >= nums[low]:
                    return helper(nums, low, mid - 1, target)
                return helper(nums, low + 1, high, target)
            else:
                if nums[high] >= target > nums[mid]:
                    return helper(nums, low + 1, high, target)
                return helper(nums, low, mid - 1, target)

        return helper(nums, 0, len(nums) - 1, target)

        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
