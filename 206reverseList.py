class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None :
            return head
        right=head.next
        left=None
        while True:
            head.next=left
            left=head
            head=right
            right=right.next
            if right is None:
                head.next=left
                return head