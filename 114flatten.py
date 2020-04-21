# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        if root is None:
            return None
        left = self.flatten(root.left)
        root.left = None
        left_tail = left
        while left_tail is not None and left_tail.right is not None:
            left_tail = left_tail.right
        right = self.flatten(root.right)
        if left_tail is not None:
            left_tail.right = right
            root.right = left
        return root

        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
