"""
1. Had done a similar problem beforem but cant recall which. Checking the intervals
2. an empty ans list, start of with first range as curr, in a for loop of 1 to l, compare 1st range with 2nd, if the start of 2nd range is smaller or equal to end of 1st range there is an overlap.
3. if there is overlap, start would be min of both and end would be max of both, these would be curr var so it can be compared with next range.
[[1,3],[2,6],[8,10],[15,18]], here after 1st 2 sets it would be 1,6 and now 1,6 shld compare to 8,10. 
4. if the overlap is not there append the curr var's and start fresh by initializing curr as say 8,10. now 8,10 will compare with 15,18.
5. at last say one case [[1,4],[4,5]], loop ends after 1,5 append it to ans and return ans.
6. one test case fails as the interval list is not sorted so interval.sort() would sort based on 0th index element.

time comp:- O(N logn) + O(N) ~ O(nlogn), n being number of intervals, nlogn for sorting.
space comp:- O(1)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        ans = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        for i in range(1, l):
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if s2 <= curr_end:
                curr_start = min(curr_start, s2)
                curr_end = max(curr_end, e2)
            else:
                ans.append([curr_start, curr_end])
                curr_start = s2
                curr_end = e2

        ans.append([curr_start, curr_end])
        return ans
