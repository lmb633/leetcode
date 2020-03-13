# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        result, _, _ = self.isvalid(root)
        return result

    def isvalid(self, root):
        if root is None:
            return True, None, None
        if root.left is None and root.right is None:
            return True, root.val, root.val
        left, left_min, left_max = self.isvalid(root.left)
        right, right_min, right_max = self.isvalid(root.right)

        flag = True
        if left_max and left_max >= root.val:
            flag = False
        if right_min and right_min <= root.val:
            flag = False

        return left and right and flag, left_min if left_min is not None else root.val, right_max if right_max is not None else root.val


class Solution2(object):
    def isValidBST(self, root):
        if root is None:
            return True
        stack = []
        last = float('-inf')
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # print(root.val, last)
            if root.val <= last:
                return False
            last = root.val
            root = root.right
            if not stack and root is None:
                return True


class Solution3(object):
    def isValidBST(self, root):
        result = self.isvalid(root, float('-inf'), float('inf'))
        return result

    def isvalid(self, root, lower, higher):
        if root is None:
            return True
        if higher <= root.val or root.val <= lower:
            return False
        if not self.isvalid(root.left, lower, root.val):
            return False
        if not self.isvalid(root.right, root.val, higher):
            return False
        return True
