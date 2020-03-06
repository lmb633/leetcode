class Solution(object):
    def findPeakElement(self, nums):
        length = len(nums)
        if length == 0:
            return None
        nums = [-2 ** 32] + nums + [-2 ** 32]
        flag = True
        i = 1
        j = length
        while i < j:
            mid = (i + j) // 2
            print(mid, i, j)
            if mid == i:
                break
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                i = mid
            elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                j = mid
            elif nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                i = mid
        return i - 1 if nums[i] > nums[j] else j - 1


# 简化代码
class Solution2(object):
    def findPeakElement(self, nums):
        length = len(nums)
        i = 0
        j = length - 1
        while i < j:
            mid = (i + j) // 2
            print(mid, i, j)
            if nums[mid] > nums[mid + 1]:
                j = mid
            else:
                i = mid + 1
        return i


solution = Solution()
a = [1,4]
print(solution.findPeakElement(a))
