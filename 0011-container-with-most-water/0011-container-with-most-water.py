"""
The 2 pointer approach

1. a left and right pointer at start and end of list.
2. if len is 2 then return the min of the list
3. else calculate the max qnt of water it can hold by min of left and right multiplied by distance between both
4. if number of left index is smaller than right then inc left else dec right and record and return the max qnt.

time comp:- o(n)
space comp :- o(1) // not using any new list
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l == 2:
            return min(height[0], height[1])
        else:
            left = 0
            right = l - 1
            qnt = 0
            while (left < right):
                qnt = max(qnt, ((right-left) * min(height[left], height[right])))
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        return qnt