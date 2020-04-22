class Solution(object):
    def search(self, nums, target):
        def helper(nums, low, high, target):
            if low > high:
                return -1
            mid = (low + high) // 2
            # print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] >= nums[low]:
                    return helper(nums, mid + 1, high, target)
                else:
                    if target <= nums[high]:
                        return helper(nums, mid + 1, high, target)
                    return helper(nums, low, mid - 1, target)
            else:
                if nums[mid] <= nums[high]:
                    return helper(nums, low, mid - 1, target)
                else:
                    if target >= nums[low]:
                        return helper(nums, low, mid - 1, target)
                    return helper(nums, mid + 1, high, target)

        return helper(nums, 0, len(nums) - 1, target)

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
