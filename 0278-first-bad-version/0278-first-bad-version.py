"""
1. running a linear search didnt work, TLE
2. used binary search for this, if the mid is bad then mid could be the first bad version or previous to mid
3. if mid is not bad, then it should be from mid+1 to n
4. calculate new mid check if it is bad until left < right
5. return left, for n==1 the while would break and return left directly which is 1

time comp:- O(logn)
space comp :- O(1)
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left