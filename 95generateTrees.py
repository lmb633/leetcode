import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        nodes = [i + 1 for i in range(n)]
        result = self.generate(nodes)
        return result

    def generate(self, nodes):
        result = []
        length = len(nodes)
        # print(length)
        if length == 0:
            return [None, ]
        for i in range(0, length):
            left = self.generate(nodes[:i])
            right = self.generate(nodes[i + 1:])
            # print(nodes[:i], nodes[i + 1:])
            # print(left, right)
            for l in left:
                for r in right:
                    root = TreeNode(nodes[i])
                    root.left = l
                    root.right = r
                    result.append(root)
        return result

    def deep_copy(self, root):
        q = queue.Queue()
        q_new = queue.Queue()
        new_tree = TreeNode(root.val)
        q.put(root)
        q_new.put(new_tree)
        while not q.empty():
            node = q.get()
            node_new = q_new.get()
            if node.left is not None:
                new_left = TreeNode(node.left.val)
                node_new.left = new_left
                q.put(node.left)
                q_new.put(new_left)
            if node.right is not None:
                new_right = TreeNode(node.right.val)
                node_new.right = new_right
                q.put(node.right)
                q_new.put(new_right)
        return new_tree


solution = Solution()
solution.generateTrees(3)
a = [None, ]
print(a)
