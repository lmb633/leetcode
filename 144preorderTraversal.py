class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        result = []
        self.preorder(root, result)
        return result

    def preorder(self, root, result):
        if root is None:
            return
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)


class Solution2(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = []
        stack = []
        while True:
            while root is not None:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
            if not stack and root is None:
                break
        return result
