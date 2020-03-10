class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_ = 0

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        self.find(root)
        return self.max_ - 1

    def find(self, root):
        if root is None:
            return 0
        left = self.find(root.left)
        right = self.find(root.right)
        if left + right + 1 > self.max_:
            self.max_ = left + right + 1
        return max(left, right) + 1
