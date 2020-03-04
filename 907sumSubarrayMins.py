# n2复杂度超时
# 子数组的最小值之和
# 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
# 由于答案可能很大，因此返回答案模 10^9 + 7。
class Solution(object):
    def sumSubarrayMins(self, A):
        result = sum(A)
        mod = 10 ** 9 + 7
        for i in range(len(A), 1, -1):
            for j in range(i - 1):
                A[j] = min(A[j], A[j + 1])
                result += A[j]
                result = result
        return result % mod


# n 复杂度
class Solution2(object):
    def sumSubarrayMins(self, A):
        result = 0
        mod = 10 ** 9 + 7
        len_a = len(A)
        left = [-1 for i in range(len_a)]
        right = [len_a for i in range(len_a)]
        order_stack = []
        for i in range(len_a):
            while order_stack and A[order_stack[-1]] > A[i]:
                order_stack.pop()
            if not order_stack:
                left[i] = -1
            else:
                left[i] = order_stack[-1]
            order_stack.append(i)
        for i in range(len_a - 1, -1, -1):
            while order_stack and A[order_stack[-1]] >= A[i]:
                order_stack.pop()
            if not order_stack:
                right[i] = len_a
            else:
                right[i] = order_stack[-1]
            order_stack.append(i)
        for i in range(len_a):
            result += (i - left[i]) * (right[i] - i) * A[i]
            result %= mod

        return result
