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
