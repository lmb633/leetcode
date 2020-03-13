class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


result_ = 0


class Solution(object):
    def pathSum(self, root, sum_):
        def helper(root, prefix, cursum):
            if root is None:
                return
            check(prefix + [root.val])
            helper(root.left, prefix + [root.val], cursum + root.val)
            helper(root.right, prefix + [root.val], cursum + root.val)

        def check(prefix):
            temp = 0
            for i in range(len(prefix) - 1, -1, -1):
                temp += prefix[i]
                if temp == sum_:
                    global result_
                    result_ += 1
        helper(root, [], 0)
        return result_