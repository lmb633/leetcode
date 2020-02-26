# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        head1 = head
        head2 = head
        for i in range(n):
            head1 = head1.next
        if head1 is None:
            return head2.next
        while head1.next is not None:
            head1 = head1.next
            head2 = head2.next
        head2.next = head2.next.next
        return head

