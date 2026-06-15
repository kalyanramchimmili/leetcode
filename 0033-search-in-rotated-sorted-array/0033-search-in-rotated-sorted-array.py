"""
1. you can run a liner search for o(n), for o(logn), its a midified binary search.
2. if the array is rotated first part of array is sorted or 2nd part is sorted like [4,5,6,7,|0,1,2,3], 2 part of the array.
3. doing a normal bs, if the value is mid return else, if num is left is < num in mid that means first part of array is sorted, check if values is in btw these if it is run a bs btw left and mid-1, else move left to mid+1.
4. If the array is not sorted till left to mid in cases like [6,7,0,1,2,3,4], such case array of right part would be sorted, check if the value is in that part of array if not move the right to mid-1 to check on left part of array.
5. if not found return, for array with 2 nums [3,1] mid would be 3 left would be 3, so nums[left] <= nums[mid]. Return -1 if not found.

Time comp:- O(logn)
space comp:- O(1)
"""
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