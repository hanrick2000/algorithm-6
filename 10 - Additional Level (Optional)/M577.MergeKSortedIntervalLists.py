"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        array = []
        for i in intervals:
            for j in i:
                array.append(j)

        array = sorted(array, key = lambda i: i.start)

        result, size = [], len(array)
        if size == 0:
            return result

        for i in range(size):
            if i != 0 and result[-1].end >= array[i].start:
                result[-1].end = max(result[-1].end, array[i].end)
            else:
                result.append(array[i])

        return result
