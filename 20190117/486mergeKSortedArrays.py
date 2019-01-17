import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        result, heap = [], []

        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue

            heapq.heappush(heap, (array[0], index, 0))

        while len(heap):
            value, i, j = heap[0]
            heapq.heappop(heap)

            result.append(value)
            if j + 1 < len(arrays[i]):
                heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

        return result
