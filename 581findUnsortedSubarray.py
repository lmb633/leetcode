class Solution(object):
    def findUnsortedSubarray(self, nums):
        if not nums or len(nums) < 1:
            return 0
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] >= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] < stack[-1][0]:
                    stack.pop()
                stack.append((nums[i], i))
        print(stack)
        left = 0
        while left < len(stack) and stack[left][1] == left:
            left += 1

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if not stack or nums[i] <= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] > stack[-1][0]:
                    stack.pop()
                stack.append((nums[i], i))
        print(stack)
        right = len(nums) - 1
        i = 0
        while i < len(stack) and stack[i][1] == right:
            right -= 1
            i += 1
        print(left, i, right)
        return right - left + 1 if right - left + 1 > 0 else 0
