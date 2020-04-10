# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 0
        while i < len(inorder):
            if inorder[i] == preorder[0]:
                break
            i += 1
        # print(i)
        left = self.buildTree(preorder[1:1 + i], inorder[0:i])
        right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        root.left = left
        root.right = right
        return root

        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
