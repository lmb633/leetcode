class Solution(object):
    def intervalIntersection(self, A, B):
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][0] <= A[i][1]:
                result.append([B[j][0], min(B[j][1], A[i][1])])
                if B[j][1] < A[i][1]:
                    j += 1
                else:
                    i += 1
            elif B[j][0] <= A[i][0] <= B[j][1]:
                result.append([A[i][0], min(A[i][1], B[j][1])])
                if B[j][1] < A[i][1]:
                    j += 1
                else:
                    i += 1
            elif A[i][1] < B[j][0]:
                i += 1
            else:
                j += 1
                # print(i,j,result)
        return result

        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """