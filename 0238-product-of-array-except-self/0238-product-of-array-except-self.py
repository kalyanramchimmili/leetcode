class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = 1
        postfix = 1
        res = [1]*l
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(l-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
"""
        l = len(nums)
        prefix = [1]*l
        postfix = [1]*l
        res = [1]*l
        for i in range(1,l):
            prefix[i] = nums[i-1]*prefix[i-1]
            
        for i in range(l-2 , -1, -1):
            postfix[i] = nums[i+1]*postfix[i+1]
        
        for i in range(l):
            res[i] = prefix[i]*postfix[i]
        return res
"""