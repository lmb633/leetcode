# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        head0 = head
        node_map = {}
        node_map[None] = None
        while head is not None:
            node_map[head] = Node(head.val)
            head = head.next
        head = head0
        while head is not None:
            node_map[head].next = node_map[head.next]
            node_map[head].random = node_map[head.random]
            head = head.next
        return node_map[head0]

        """
        :type head: Node
        :rtype: Node
        """
