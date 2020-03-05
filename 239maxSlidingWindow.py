from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        len_nums = len(nums)
        if len_nums == 0 or k == 0:
            return []
        dq = deque()
        result = []
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            print(dq)
        result.append(nums[dq[0]])
        for i in range(k, len_nums):
            if dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            result.append(nums[dq[0]])
        return result


solution = Solution()
a = [1, 3, -1, -3, 5, 3, 6, 7]
print('result', solution.maxSlidingWindow(a, 3))
