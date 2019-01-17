"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        result, index = [], 0

        while index < len(intervals) and intervals[index].start < newInterval.start:
            index += 1

        intervals.insert(index, newInterval)

        last = None

        for iterval in intervals:
            if last is None or last.end < iterval.start:
                result.append(iterval)
                last = iterval
            else:
                last.end = max(last.end, iterval.end)

        return result
