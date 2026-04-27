class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        len_num = len(nums)
        i = 0
        j = len_num - 1
        while i < j:
            s = sorted_nums[i] + sorted_nums[j]
            if s > target:
                j = j - 1
            elif s < target:
                i = i + 1
            else:
                val_i, val_j = sorted_nums[i], sorted_nums[j]
                ind_i = nums.index(val_i)
                ind_j = nums.index(val_j, ind_i + 1) if val_i == val_j else nums.index(val_j)
                return [ind_i, ind_j]
