class Solution(object):
    def canThreePartsEqualSum(self, A):
        i = 0
        j = len(A) - 1
        if j < 2:
            return False
        if sum(A) % 3 != 0:
            return False
        avg = sum(A) // 3
        left = A[i]
        mid = sum(A[1:-1])
        right = A[j]
        while i < j - 1:
            # print(i, j, left, mid, right)
            while right != avg and j - 1 > i:
                j -= 1
                mid -= A[j]
                right += A[j]
            while left != avg and i < j - 1:
                i += 1
                mid -= A[i]
                left += A[i]
            if left == mid == right and i < j - 1:
                return True
            i += 1
            j -= 1
            mid -= A[j]
            right += A[j]
            mid -= A[i]
            left += A[i]
        return False


solution = Solution()
a = [1, -1, 1, -1]
print(solution.canThreePartsEqualSum(a))
