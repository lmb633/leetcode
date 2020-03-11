class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if root is None:
            return
        if root.left is not None:
            self.inorder(root.left)
        self.result.append(root.val)
        if root.right is not None:
            self.inorder(root.right)


class Solution2(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
            if not stack and root is None:
                break
        return result
