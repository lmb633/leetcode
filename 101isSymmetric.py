class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        left = root.left
        right = root.right
        return self.compare(left, right)

    def compare(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)
