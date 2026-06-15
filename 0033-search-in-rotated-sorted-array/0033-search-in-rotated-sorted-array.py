class Solution:
    def search(self, nums: List[int], value: int) -> int:
        l = len(nums)
        left = 0
        right = l-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == value:
                return mid
            # First part of array is sorted    
            elif nums[left] <= nums[mid]:
                if nums[left] <= value < nums[mid]:
                    right = mid - 1
                else:
                    left = mid+1
            # right part of array is sorted
            else:
                if nums[mid] < value <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1