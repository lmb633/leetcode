class Solution(object):
    def findKthLargest(self, nums, k):
        length = len(nums)
        k = length - k
        return self.find(nums, 0, length - 1, k)

    def find(self, nums, left, right, k):
        if left >= right:
            return nums[left]
        temp = nums[left]
        i = left
        j = right
        print(i, j, k)
        while i < j:
            while nums[j] > temp and i < j:
                j -= 1
            if i < j:
                nums[i] = nums[j]
            while nums[i] <= temp and i < j:
                i += 1
            if i < j:
                nums[j] = nums[i]
        nums[i] = temp
        print(i, j, k)
        if i == k:
            return nums[i]
        elif i > k:
            return self.find(nums, left, i - 1, k)
        else:
            return self.find(nums, i + 1, right, k)


a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
solution = Solution()
print('result', solution.findKthLargest(a, 4))
