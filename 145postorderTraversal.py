class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, root, result):
        if root is None:
            return
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)


class Solution2(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        result = []
        stack = []
        last = TreeNode(-1)
        print('begin')
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[-1]
            if root.right is None or root.right == last:
                result.append(root.val)
                last = stack.pop()
                root = None
            else:
                root = root.right
            if not stack and root is None:
                break
            print(result, stack)
        return result


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node1.left = node3
    solution = Solution2()
    print(solution.postorderTraversal(node1))
