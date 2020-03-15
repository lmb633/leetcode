class Solution(object):
    def lengthOfLIS(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        result = [1 for i in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    if result[j] > result[i] - 1:
                        result[i] = result[j] + 1
        return max(result)


class Solution2(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        max_len = 1
        stack = []
        stack.append(nums[0])
        for num in nums:
            if stack[-1] < num:
                stack.append(num)
                if len(stack) > max_len:
                    max_len = len(stack)
            elif stack[-1] > num:
                idx = self.find(stack, 0, len(stack) - 1, num)
                # print(stack,idx,num)
                if stack[idx] > num:
                    stack[idx] = num
                elif stack[idx] < num:
                    stack[idx + 1] = num
                    # print(stack)
        return max_len

    def find(self, nums, low, high, target):
        if low >= high:
            return low
        mid = (low + high) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find(nums, low, mid - 1, target)
        else:
            return self.find(nums, mid + 1, high, target)
