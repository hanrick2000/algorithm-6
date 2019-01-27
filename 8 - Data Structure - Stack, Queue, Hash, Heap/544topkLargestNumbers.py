import heapq

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        results, heap = [], []
        for num in nums:
            heapq.heappush(heap, (-num))

        for i in range(k):
            results.append(-heapq.heappop(heap))
        return results
