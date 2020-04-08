# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None
        head, tail = self.get_mid(head)
        print(head.val, tail.val)
        if tail is head:
            return TreeNode(head.val)
        root = TreeNode(tail.val)
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(tail.next)
        # print('left,right',left,right)
        root.left = left
        root.right = right
        return root

    def get_mid(self, head):
        head1 = ListNode(0)
        head1.next = head
        head2 = head
        # 确保head1走到中间元素的上一个，因为需要把链表断开，然后mid为中间元素，即head1.next
        if head2 is not None:
            head2 = head2.next
        while head2 is not None:
            head1 = head1.next
            head2 = head2.next
            if head2 is not None:
                head2 = head2.next
        mid = head1.next
        head1.next = None
        return head, mid


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    solution.sortedListToBST(node1)
