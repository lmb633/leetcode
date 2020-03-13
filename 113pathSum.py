class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        result = []
        self.helper(root, [], sum, result)
        return result

    def helper(self, root, path, sum_, result):
        if root is None:
            return
        if root.left is None and root.right is None and sum_ - root.val == 0:
            path.append(root.val)
            result.append(path)
        else:
            path.append(root.val)
            path2=[i for i in path]
            self.helper(root.left, path, sum_ - root.val, result)
            self.helper(root.right, path2, sum_ - root.val, result)
