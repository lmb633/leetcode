# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, i, j):
        if i > j:
            return None
        if i == j:
            return TreeNode(nums[i])
        mid = (i + j) // 2
        print(i, mid, j)
        left = self.helper(nums, i, mid - 1)
        right = self.helper(nums, mid + 1, j)
        root = TreeNode(nums[mid])
        root.left = left
        root.right = right

        return root


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, ]
    solution = Solution()
    print(solution.sortedArrayToBST(a))
