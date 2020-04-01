# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        fast = head.next
        low = head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                low = low.next
        # print(low.val)
        temp = low.next
        low.next = None
        # print(head,temp)
        left = self.sortList(head)
        right = self.sortList(temp)
        head0 = ListNode(0)
        head = head0
        while left is not None and right is not None:
            if left.val < right.val:
                head.next = left
                head = head.next
                left = left.next
            else:
                head.next = right
                head = head.next
                right = right.next
        if left is not None:
            head.next = left
        if right is not None:
            head.next = right
        return head0.next

        """
        :type head: ListNode
        :rtype: ListNode
        """