class Solution(object):
    def peakIndexInMountainArray(self, A):
        length = len(A)
        i = 0
        j = length - 1
        while i < j:
            mid = (i + j) // 2
            if A[mid] > A[mid + 1]:
                j = mid
            else:
                i = mid + 1
        return i
        """
        :type A: List[int]
        :rtype: int
        """