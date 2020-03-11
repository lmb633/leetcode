import queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        q1 = queue.Queue()
        q1.put(root)
        while not q1.empty():
            temp = []
            q2 = queue.Queue()
            while not q1.empty():
                node = q1.get()
                temp.append(node.val)
                if node.left is not None:
                    q2.put(node.left)
                if node.right is not None:
                    q2.put(node.right)
            result.append(temp)
            q1 = q2
        return result
