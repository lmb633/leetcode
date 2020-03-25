class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        right = head.next
        left = None
        while True:
            head.next = left
            left = head
            head = right
            right = right.next
            if right is None:
                head.next = left
                return head


class Solution2(object):
    def reverseList(self, head):
        head0 = None
        while head is not None:
            temp = head
            head = head.next
            temp.next = head0
            head0 = temp
        return head0


class Solution3(object):
    def reverseList(self, head):
        if head is None:
            return None
        tail, head0 = self.helper(head)
        tail.next = None
        return head0

    def helper(self, head):
        if head.next is None:
            return head, head
        tail, head0 = self.helper(head.next)
        tail.next = head
        print(head.val, tail.val, head0.val)
        return head, head0


import time

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution3()
head = solution.reverseList(node1)
while head is not None:
    print(head.val)
    head = head.next
    time.sleep(1)
