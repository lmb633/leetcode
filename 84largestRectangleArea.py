class Solution(object):
    def largestRectangleArea(self, heights):
        max_matrix = 0
        stack = []
        i = 0
        while i < len(heights):
            last = None
            while stack and stack[-1][0] >= heights[i]:
                matrix1 = stack[-1][0] * (i - stack[-1][1])
                matrix2 = heights[i] * (i - stack[-1][1] + 1)
                matrix = max(matrix1, matrix2)
                if matrix > max_matrix:
                    max_matrix = matrix
                last = stack.pop()
            if last is not None:
                stack.append((heights[i], last[1]))
            else:
                stack.append((heights[i], i))
            i += 1
            # print(stack,max_matrix,i)
        for j in range(len(stack)):
            matrix = stack[j][0] * (i - stack[j][1])
            if matrix > max_matrix:
                max_matrix = matrix

        return max_matrix
        """
        :type heights: List[int]
        :rtype: int
        """