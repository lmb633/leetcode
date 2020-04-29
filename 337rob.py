# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归超时
class Solution(object):
    def rob(self, root):
        if root is None:
            return 0
        left_sum = 0
        if root.left is not None:
            left = root.left
            left_sum = self.rob(left.left) + self.rob(left.right)
        right_sum = 0
        if root.right is not None:
            right = root.right
            right_sum = self.rob(right.left) + self.rob(right.right)
        return max(root.val + right_sum + left_sum, self.rob(root.left) + self.rob(root.right))


# 添加一个visited记录已访问顶点
class Solution2(object):
    def __init__(self):
        self.visited = {}

    def rob(self, root):
        if root in self.visited:
            return self.visited[root]
        if root is None:
            return 0
        left_sun_sum = 0
        if root.left is not None:
            left = root.left
            left_sun_sum = self.rob(left.left) + self.rob(left.right)
        right_sun_sum = 0
        if root.right is not None:
            right = root.right
            right_sun_sum = self.rob(right.left) + self.rob(right.right)
        self.visited[root] = max(root.val + right_sun_sum + left_sun_sum, self.rob(root.left) + self.rob(root.right))
        return self.visited[root]


# 上述方法弊端是每一步要递归访问6个点，左右，左右的左右
# 优化方法是每步值访问左右两个结点，并记录两种状态
class Solution3(object):
    def rob(self, root):
        def helper(root):
            if root is None:
                return [0, 0]
            left = helper(root.left)
            right = helper(root.right)
            result1 = root.val + left[1] + right[1]
            result2 = max(left) + max(right)
            return [result1, result2]

        return max(helper(root))
