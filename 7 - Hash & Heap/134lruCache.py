class LinkedNode:
    def __init__(self, key = None, value = None):
        self.key, self.value, self.prev, self.next = key, value, None, None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.tail.prev = self.head
        self.head.next = self.tail

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash:
            return -1

        self.moveToTail(key)

        return self.tail.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if self.get(key) != -1:
            node = self.hash.get(key)
            node.value = value
            return

        if len(self.hash) < self.capacity:
            node = LinkedNode(key, value)
            self.hash[key] = node

            if self.head.key is None:
                self.head = node
            self.moveToTail(key)

            return

        if self.head.key:
            self.hash.pop(self.head.key)
        self.head.key, self.head.value = key, value
        self.hash[key] = self.head
        self.moveToTail(key)

    def moveToTail(self, key):
        node = self.hash.get(key)

        if self.tail == node:
            return

        if node.prev is not None and node.prev.key is not None:
            node.prev.next = node.next

        if node.next is not None:
            if self.head == node:
                self.head = node.next
            node.next.prev = node.prev

        node.prev, self.tail.next, node.next = self.tail, node, self.tail.next
        node.prev.next = node

        self.tail = node
