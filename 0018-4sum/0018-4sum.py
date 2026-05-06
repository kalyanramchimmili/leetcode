"""
1. waiting for leetcode to drop 5-sum next, but coming to solution still the 2 pointer solution with 2 fixed values and 2 pointers
2. 2 for loops with f1 and f2 as 2 fixed values, left and right pointers, the que is bit confusing, but they want unique indices and values. The framing of que is stupid
3. first loop iterates from 0 to l-3 and 2nd loop 0 to l-2, during each loop we have left and right var, if sum is equal to target append the list to ans list, then inc left and right. To skip duplicates, check if prev left and inc left is same if yes inc, and same for right if prev right and dec right is same, dec right again.
4. same logic if sum is less than target, then inc left until its prev value is not same and same for right keep dec right is sum is greater than target
5. to skip duplicates in top, if f1 is > 0 and if it is same as prev one skip, same for f2 is greater than starting pos and prev pos is same skip that pos

time comp:- 2 loops n-3*n-2 and each loop is doing n-2 ~ O(n^3)
space comp:- o(1)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        ans_list = []

        if target <= 0 and nums[0] > 0:
            return []

        for f1 in range(0, l - 3):
            if f1 > 0 and nums[f1] == nums [f1-1]:
                continue
            for f2 in range(f1 + 1, l - 2):
                if f2 > f1+1 and nums[f2] == nums[f2-1]:
                    continue
                left = f2 + 1
                right = l - 1
                while left < right:
                    curr_sum = nums[f1] + nums[f2] + nums[left] + nums[right]
                    if curr_sum == target:
                        ans_list.append([nums[f1], nums[f2], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        
                    elif curr_sum < target:
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return ans_list
