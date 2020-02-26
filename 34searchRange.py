class Solution(object):
    def searchRange(self, nums, target):
        i = 0
        j = len(nums) - 1
        index = -1
        while i <= j:
            mid = int((i + j) / 2)
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        if index == -1:
            return [-1, -1]
        s = index - 1
        while s >= 0:
            if nums[s] == target:
                s -= 1
            else:
                break
        e = index + 1
        while e <= len(nums) - 1:
            if nums[e] == target:
                e += 1
            else:
                break
        return [s + 1, e - 1]


solution = Solution()
nums = [1, 2, 3, 4, 5, 5, 5, 5, 6]
print(solution.searchRange(nums, 5))
