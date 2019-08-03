class TwoSum:
    def __init__(self):
        self.nums = {}

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for number, count in self.nums.items():
            if value - number in self.nums and (value - number != number or count > 1):
                return True

        return False
