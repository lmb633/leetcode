class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        heada = headA
        headb = headB
        a = 1
        b = 1
        while heada.next is not None:
            a += 1
            heada = heada.next
        while headb.next is not None:
            b += 1
            headb = headb.next
        diff = abs(a - b)
        heada = headA
        headb = headB
        if a > b:
            for i in range(diff):
                heada = heada.next
        if b > a:
            for i in range(diff):
                headb = headb.next
        while heada is not None and headb is not None:
            if heada == headb:
                return heada
            heada = heada.next
            headb = headb.next
        return None

        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
