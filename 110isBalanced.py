# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.flag = True

    def isBalanced(self, root):
        self.help_f(root)
        return self.flag

    def help_f(self, root):
        if not self.flag:
            return 0
        if root is None:
            return 0
        left = self.help_f(root.left)
        right = self.help_f(root.right)
        if abs(left - right) > 1:
            self.flag = False
            return 0
        else:
            return max(left, right) + 1
