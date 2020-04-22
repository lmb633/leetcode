# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        head0 = ListNode(0)
        head0.next = head
        slow = fast = head0
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
                if fast == slow:
                    while fast != head0:
                        head0 = head0.next
                        fast = fast.next
                    return fast
        return None
        """
        :type head: ListNode
        :rtype: ListNode
        """
