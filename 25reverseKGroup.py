# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        right = head
        head0 = ListNode(0)
        head0.next = head
        left = head0
        flag = True
        while True:
            for i in range(k):
                temp = right
                if right is not None:
                    right = right.next
                else:
                    flag = False
            if flag is False:
                break
            temp.next = None
            # print(left.val,head.val,temp.val,right.val)
            head_temp, tail_temp = self.reverse(head)
            # print(head_temp.val,tail_temp.val)
            left.next = head_temp
            tail_temp.next = right
            head = right
            left = tail_temp
        return head0.next

    def reverse(self, head):
        tail = head
        head0 = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = head0
            head0 = temp
        return head0, tail

        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """