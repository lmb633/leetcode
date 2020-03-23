# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        result = []
        queue = []
        queue.append(root)
        while queue:
            temp = []
            queue2 = []
            for node in queue:
                if node is not None:
                    temp.append(node.val)
                    queue2.append(node.left)
                    queue2.append(node.right)
            if temp:
                result.append(temp)
            queue = queue2
        return result

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
