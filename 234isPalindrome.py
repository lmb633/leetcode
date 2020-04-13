# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        head0 = ListNode(0)
        head0.next = head
        slow = fast = head0
        i = 0
        while fast is not None:
            fast = fast.next
            i += 1
            if fast is not None:
                fast = fast.next
                slow = slow.next
                i += 1
        # print(i)
        head2 = slow.next
        # print(head2.val)
        slow.next = None
        head0.next = None

        head0 = None
        while head is not None:
            temp = head.next
            head.next = head0
            head0 = head
            head = temp
        # print(head0.val)
        if (i - 1) % 2 == 1:
            head0 = head0.next

        while head0 is not None and head2 is not None:
            if head0.val != head2.val:
                return False
            head0 = head0.next
            head2 = head2.next
        return True

        """
        :type head: ListNode
        :rtype: bool
        """
