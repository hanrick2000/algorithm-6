class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here

        # method 3: Divide Conquer
        n = len(A) + len(B)
        if n % 2 == 0:
            return (self.findKth(A, B, n // 2) + self.findKth(A, B, n // 2 + 1)) / 2

        return self.findKth(A, B, n // 2 + 1)

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]

        start, end = min(A[0], B[0]), max(A[len(A) - 1], B[len(B) - 1])
        while start + 1 < end:
            mid = (start + end) // 2
            if self.countSmallerOrEqual(A, mid) + self.countSmallerOrEqual(B, mid) < k:
                start = mid
            else:
                end = mid
        if self.countSmallerOrEqual(A, start) + self.countSmallerOrEqual(B, start) >= k:
            return start

        return end

    def countSmallerOrEqual(self, array, number):
        start, end = 0, len(array) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if array[mid] <= number:
                start = mid
            else:
                end = mid

        if array[start] > number:
            return start

        if array[end] > number:
            return end

        return len(array)

    #     # method 2: FindKth
    #     n = len(A) + len(B)
    #     if n % 2 == 0:
    #         return (self.findKth(A, 0, B, 0, n // 2) + self.findKth(A, 0, B, 0, n // 2 + 1)) / 2

    #     return self.findKth(A, 0, B, 0, n // 2 + 1)

    # def findKth(self, A, startOfA, B, startOfB, k):
    #     if startOfA >= len(A):
    #         return B[startOfB + k - 1]
    #     if startOfB >= len(B):
    #         return A[startOfA + k - 1]

    #     if k == 1:
    #         return min(A[startOfA], B[startOfB])

    #     if startOfA + k // 2 - 1 < len(A):
    #         halfKthOfA = A[startOfA + k // 2 - 1]
    #     else:
    #         halfKthOfA = sys.maxsize

    #     if startOfB + k // 2 - 1 < len(B):
    #         halfKthOfB = B[startOfB + k // 2 - 1]
    #     else:
    #         halfKthOfB = sys.maxsize

    #     if halfKthOfA < halfKthOfB:
    #         return self.findKth(A, startOfA + k // 2, B, startOfB, k - k // 2)

    #     return self.findKth(A, startOfA, B, startOfB + k // 2, k - k // 2)

#         # method 1: based on median comparison
#         return self.findMedian(PartialArray(A), PartialArray(B))

#     def findMedian(self, A, B):
#         while not A.isEmpty() and not B.isEmpty():
#             if A.size() == 1 and B.size() == 1:
#                 return (A.getMedian() + B.getMedian()) / 2

#             if A.getLowerMedian() > B.getLowerMedian():
#                 lowerArray = B
#             else:
#                 lowerArray = A
#             if A.getUpperMedian() <= B.getUpperMedian():
#                 upperArray = B
#             else:
#                 upperArray = A

#             lowerIndex, upperIndex = lowerArray.getLowerMedianIndex(), upperArray.getUpperMedianIndex()

#             numOfRemoved = min(lowerArray.getNumOfLower(lowerIndex), upperArray.getNumOfUpper(upperIndex))

#             lowerArray.removeLower(numOfRemoved)
#             upperArray.removeUpper(numOfRemoved)

#         if A.isEmpty():
#             return B.getMedian()

#         return A.getMedian()

# class PartialArray:
#     def __init__(self, array):
#         self.array = array
#         self.start = 0
#         self.end = len(self.array) - 1

#     def getLowerMedianIndex(self):
#         return (self.start + self.end) // 2

#     def getLowerMedian(self):
#         return self.array[(self.start + self.end) // 2]

#     def getUpperMedianIndex(self):
#         return (self.start + self.end + 1) // 2

#     def getUpperMedian(self):
#         return self.array[(self.start + self.end + 1) // 2]

#     def size(self):
#         return self.end - self.start + 1

#     def getMedian(self):
#         return (self.getUpperMedian() + self.getLowerMedian()) / 2

#     def isEmpty(self):
#         return self.size() == 0

#     def getNumOfUpper(self, index):
#         if index == self.end:
#             return 1

#         return self.end - index

#     def getNumOfLower(self, index):
#         if index == self.start:
#             return 1

#         return index - self.start

#     def removeLower(self, numOfRemoved):
#         self.start += numOfRemoved

#     def removeUpper(self, numOfRemoved):
#         self.end -= numOfRemoved

#     def get(self, index):
#         return self.array[index]
