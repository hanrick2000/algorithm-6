class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        return self.findMedian(PartialArray(A), PartialArray(B))

    def findMedian(self, A, B):
        while not A.isEmpty() and not B.isEmpty():
            if A.size() == 1 and B.size() == 1:
                return (A.getMedian() + B.getMedian()) / 2

            if A.getLowerMedian() > B.getLowerMedian():
                lowerArray = B
            else:
                lowerArray = A
            if A.getUpperMedian() <= B.getUpperMedian():
                upperArray = B
            else:
                upperArray = A

            lowerIndex, upperIndex = lowerArray.getLowerMedianIndex(), upperArray.getUpperMedianIndex()

            numOfRemoved = min(lowerArray.getNumOfLower(lowerIndex), upperArray.getNumOfUpper(upperIndex))

            lowerArray.removeLower(numOfRemoved)
            upperArray.removeUpper(numOfRemoved)

        if A.isEmpty():
            return B.getMedian()

        return A.getMedian()

class PartialArray:
    def __init__(self, array):
        self.array = array
        self.start = 0
        self.end = len(self.array) - 1

    def getLowerMedianIndex(self):
        return (self.start + self.end) // 2

    def getLowerMedian(self):
        return self.array[(self.start + self.end) // 2]

    def getUpperMedianIndex(self):
        return (self.start + self.end + 1) // 2

    def getUpperMedian(self):
        return self.array[(self.start + self.end + 1) // 2]

    def size(self):
        return self.end - self.start + 1

    def getMedian(self):
        return (self.getUpperMedian() + self.getLowerMedian()) / 2

    def isEmpty(self):
        return self.size() == 0

    def getNumOfUpper(self, index):
        if index == self.end:
            return 1

        return self.end - index

    def getNumOfLower(self, index):
        if index == self.start:
            return 1

        return index - self.start

    def removeLower(self, numOfRemoved):
        self.start += numOfRemoved

    def removeUpper(self, numOfRemoved):
        self.end -= numOfRemoved

    def get(self, index):
        return self.array[index]
