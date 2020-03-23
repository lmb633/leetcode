# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        head0=head
        if head0 is  None:
            return None
        num=0
        while head0 is not None:
            head0=head0.next
            num+=1
        for i in range(num//2):
            head=head.next
        return head


        """
        :type head: ListNode
        :rtype: ListNode
        """