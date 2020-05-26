class Node():
    def __init__(self, val, key=None):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None


class BiLinkedList():
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add_head(self, node):
        temp = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = temp
        temp.pre = node

    def del_node(self, node=None):
        if self.head.next == self.tail:
            return -1
        if node is None:
            node = self.tail.pre
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = node.pre = None
        return node


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.list = BiLinkedList()

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            self.list.del_node(node)
            self.list.add_head(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.data:
            node = self.data[key]
            self.list.del_node(node)
            self.list.add_head(node)
            node.val = value
            return
        if self.capacity <= 0:
            node = self.list.del_node()
            self.data.pop(node.key)
            self.capacity += 1
        node = Node(value, key)
        self.data[key] = node
        self.list.add_head(node)
        self.capacity -= 1


if __name__ == '__main__':
    cache = LRUCache(2)

    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    # link = BiLinkedList()
    # node1 = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # link.add_head(node1)
    # link.add_head(node2)
    # link.add_head(node3)
    # print(link.head.val, link.tail.val, link.head.next.val, link.tail.pre.val)
    # print(link.del_node(node3).val)
    # print(link.head.val, link.tail.val)
    # print(link.del_node(node1).val)
    # print(link.head.val, link.tail.val)
    # print(link.del_node().val)
    # print(link.head.val, link.tail.val)
