class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.size = 0
        self.frontIndex, self.rearIndex = 0, -1
        self.queue = [None] * n

    """
    @return:  return true if the array is full
    """
    def isFull(self):
        # write your code here
        return self.size == len(self.queue)

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        # write your code here
        return self.size == 0

    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        # write your code here
        if self.isFull():
            raise Exception("Queue is already full!")

        self.rearIndex = (self.frontIndex + self.size) % len(self.queue)
        self.queue[self.rearIndex] = element
        self.size += 1

    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        # write your code here
        if self.isEmpty():
            raise Exception("Queue is already empty!")

        item = self.queue[self.frontIndex]
        self.frontIndex = (self.frontIndex + 1) % len(self.queue)
        self.size -= 1

        return item
