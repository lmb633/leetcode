# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result0 = ListNode(0)
        result = result0
        while l1 is not None and l2 is not None:
            # print(l1.val,l2.val)
            if l2.val >= l1.val:
                result.next = l1
                l1 = l1.next
                result = result.next
            else:
                result.next = l2
                l2 = l2.next
                result = result.next
        if l2 is not None:
            result.next = l2
        if l1 is not None:
            result.next = l1
        return result0.next