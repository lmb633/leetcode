class Solution(object):
    def sortColors(self, nums):
        length = len(nums)
        left = 0
        right = length - 1
        i = 0
        while i <= right:
            if nums[i] == 2:
                nums[i] = nums[right]
                nums[right] = 2
                right -= 1
            elif nums[i] == 0:
                nums[i] = nums[left]
                nums[left] = 0
                left += 1
                i += 1
            else:
                i += 1
                # print(left,i,right,nums)
        return nums
