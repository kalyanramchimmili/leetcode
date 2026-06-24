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
