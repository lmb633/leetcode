class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        idx1=head
        idx2=head.next
        head=head.next
        head0=ListNode(-1)
        while True:
            head0.next=idx2
            idx1.next=idx2.next
            idx2.next=idx1
            if idx1.next is None or idx1.next.next is None:
                return head
            else:
                head0=idx1
                idx1=idx1.next
                idx2=idx1.next

