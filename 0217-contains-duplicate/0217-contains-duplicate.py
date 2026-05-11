"""
1. A hashmap count to cound the instances
2. if count is greater than 1 for any number in nums, return true
3. if the loop is completed, it exits then return False as there is duplicate

Time comp:- O(N), N being number of int in nums
Space comp:- O(N), hashmap space
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
            if count[i] > 1:
                return True
            
        return False
        