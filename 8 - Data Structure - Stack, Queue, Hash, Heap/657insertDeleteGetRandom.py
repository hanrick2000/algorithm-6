import random

class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.data = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.data:
            return False

        self.data.add(val)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.data:
            return False

        self.data.remove(val)
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        index = random.randint(0, len(self.data) - 1)
        return list(self.data)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
