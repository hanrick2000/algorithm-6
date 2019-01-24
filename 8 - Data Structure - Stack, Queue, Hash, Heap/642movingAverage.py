# method 2
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = collections.deque()
        self.size = size
        self.sum = 0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        self.sum += val

        if len(self.queue) >= self.size:
            self.sum -= self.queue.popleft()

        self.queue.append(val)

        return self.sum / len(self.queue)

# # method 1
# import queue

# class MovingAverage:
#     """
#     @param: size: An integer
#     """
#     def __init__(self, size):
#         # do intialization if necessary
#         self.queue = queue.Queue()
#         self.size = size
#         self.sum = 0

#     """
#     @param: val: An integer
#     @return:
#     """
#     def next(self, val):
#         # write your code here
#         self.sum += val

#         if self.queue.qsize() >= self.size:
#             self.sum -= self.queue.get()

#         self.queue.put(val)

#         return self.sum / self.queue.qsize()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
