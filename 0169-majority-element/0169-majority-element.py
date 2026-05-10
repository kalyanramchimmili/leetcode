class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        l = len(nums)//2
        for i in nums:
            temp = count.get(i) if count.get(i) else 0
            count[i] = temp + 1
            if temp >= l:
                return i

        