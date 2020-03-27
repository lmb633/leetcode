class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        inedge = [0] * n
        for node in leftChild:
            if node != -1:
                inedge[node] += 1
        for node in rightChild:
            if node != -1:
                inedge[node] += 1
        i = 0
        head = None
        for edge in inedge:
            if edge > 1:
                return False
            if edge == 0:
                head = inedge[i]
                i += 1
        if i != 1:
            return False
        if head is not None:
            i = 0
            stack = []
            stack.append(head)
            visited = set()
            visited.add(head)
            while stack:
                i += 1
                node = stack.pop()
                left = leftChild[node]
                right = rightChild[node]
                if left != -1 and left not in visited:
                    stack.append(left)
                    visited.add(left)
                if right != -1 and right not in visited:
                    stack.append(right)
                    visited.add(right)
            if i < n:
                return False
            return True

        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

