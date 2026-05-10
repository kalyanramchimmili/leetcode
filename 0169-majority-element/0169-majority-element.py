"""
1. similar to ransom note problem, have a count hashmap
2. inc the count, if count of an element is more than half of the list, then return the num
3. as per que there is majority element always hence no need to handle any other case

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        l = len(nums)//2
        for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] > l:
                return i

        