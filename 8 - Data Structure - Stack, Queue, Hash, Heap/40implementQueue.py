class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1, self.stack2 = [], []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack2 = []
        for i in range(len(self.stack1) - 1, -1, -1):
            self.stack2.append(self.stack1[i])
        self.stack2.append(element)

        self.stack1 = []
        for i in range(len(self.stack2) - 1, -1, -1):
            self.stack1.append(self.stack2[i])

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.stack1.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack1[-1]
