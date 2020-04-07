# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        head0 = ListNode(0)
        head0.next = head
        pre = head0
        while head is not None:
            if head.val == val:
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return head0.next
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
