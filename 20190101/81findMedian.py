import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []

        # method two
        self.maxHeap, self.minHeap, medians = [], [], []
        for num in nums:
            self.add(num)
            medians.append(self.median)

        return medians

    @property
    def median(self):
        return -self.maxHeap[0]

    def add(self, num):
        if len(self.maxHeap) <= len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) == 0 or len(self.minHeap) == 0:
            return

        if self.median > self.minHeap[0]:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    #     # method one
    #     self.median = nums[0]
    #     self.maxHeap, self.minHeap, self.medians = [], [], []

    #     for i in range(len(nums)):
    #         if i > 0:
    #             self.add(nums[i])

    #         self.medians.append(self.median)

    #     return self.medians

    # def add(self, num):
    #     if num < self.median:
    #         heapq.heappush(self.maxHeap, -num)
    #     else:
    #         heapq.heappush(self.minHeap, num)

    #     if len(self.maxHeap) > len(self.minHeap):
    #         heapq.heappush(self.minHeap, self.median)
    #         self.median = -heapq.heappop(self.maxHeap)
    #     elif len(self.maxHeap) + 1 < len(self.minHeap):
    #         heapq.heappush(self.maxHeap, -self.median)
    #         self.median = heapq.heappop(self.minHeap)
