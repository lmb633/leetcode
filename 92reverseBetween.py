# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        i = 1
        j = m
        left = ListNode(0)
        left.next = head
        head = left
        while i < m:
            left = left.next
            i += 1
        tail = left.next

        head1 = tail
        head0 = None
        while j <= n:
            temp = head1
            head1 = head1.next
            temp.next = head0
            head0 = temp
            j += 1
        print(head0.val, tail.val, head1.val)
        left.next = head0
        tail.next = head1
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.reverseBetween(node1, 2, 3)
