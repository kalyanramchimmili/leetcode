"""
1. I was trying to do the sliding window technique, similar to max substring, using greedy to slide the left and right pointers.
2. But that dosent work, and for problem like this we need kadence algorithm

3. current and maximum starts at first index, current determines if it needs to continue with the subarray or start fresh
4. max(nums[i], nums[i]+current) for -50 2 5, at -2 it choose max(2, -48), it will choose 2
5. maximum records the max current, and returns it and end of loop.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current+nums[i])
            maximum = max(maximum, current)
        return maximum