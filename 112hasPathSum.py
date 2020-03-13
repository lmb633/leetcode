class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        return self.helper(root, sum)

    def helper(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and sum - root.val == 0:
            return True
        else :
            return self.helper(root.left, sum - root.val) or self.helper(root.right, sum - root.val)
