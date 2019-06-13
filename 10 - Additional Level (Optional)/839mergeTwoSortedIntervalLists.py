"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        results, i, j = [], 0, 0

        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.merge(results, list1[i])
                i += 1
            else:
                self.merge(results, list2[j])
                j += 1

        while i < len(list1):
            self.merge(results, list1[i])
            i += 1

        while j < len(list2):
            self.merge(results, list2[j])
            j += 1

        return results

    def merge(self, results, interval):
        if not results:
            return results.append(interval)

        last_interval = results[-1]
        if last_interval.end < interval.start:
            return results.append(interval)

        results[-1].end = max(last_interval.end, interval.end)
