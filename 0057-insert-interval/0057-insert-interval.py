"""
1. Tricky problem, but was easier you see how to compare
case 1:- before the interval if last element of current interval is less than new interval no overlap it is before, append it to ans
case 2:- if first element of current interval is greater than last element of new interval then the interval is after new interval, so append the new interval first and the current interval later
case 3:- overlap, here we choose min of first element and max of last element to make new newInterval, to check again.

if the loop is complete append the new interval, the trickiest part is in case 2 we append new interval and we append the interval, but at last we append new interval again, we cannot break, what if new interval is not before the last interval rather it is before mid interval, we would miss rest of it.

we change the newinterval to the current interval in case 2 to continue look further and we append it last anyways.

time comp:- O(N)
space comp:- O(N), N being number of intervals.
"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        ans.append(newInterval)
        return ans
