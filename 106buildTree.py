# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        i = 0
        while i < len(inorder):
            if inorder[i] == postorder[-1]:
                break
            i += 1
        left = self.buildTree(inorder[0:i], postorder[0:i])
        right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        root.left = left
        root.right = right
        return root

        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
