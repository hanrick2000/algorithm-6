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

        # method 2
        result, index = [], 0

        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
                index += 1
            elif newInterval.end < interval.start:
                result.append(interval)
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)

        result.insert(index, newInterval)
        return result

        # # method 1
        # result, index = [], 0

        # while index < len(intervals) and intervals[index].start < newInterval.start:
        #     index += 1

        # intervals.insert(index, newInterval)

        # last = None

        # for iterval in intervals:
        #     if last is None or last.end < iterval.start:
        #         result.append(iterval)
        #         last = iterval
        #     else:
        #         last.end = max(last.end, iterval.end)

        # return result
