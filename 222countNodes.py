class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        depth_left = 0
        depth_right = 0
        root1 = root
        root2 = root
        while root1.left is not None:
            root1 = root1.left
            depth_left += 1
        while root2.right is not None:
            root2 = root2.right
            depth_right += 1
        if depth_right == depth_left:
            return 1 + 2 * (2 ** depth_left - 1)
        else:
            return 1 + self.countNodes(root.left) + 1 + self.countNodes(root.right)
