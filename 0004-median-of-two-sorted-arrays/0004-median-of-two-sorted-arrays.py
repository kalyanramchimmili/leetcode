"""
1. Find the median, was pretty direct - combine the l2 with l1 and sort the array
2. the usual check of it is odd then return middle number, if not avg of mid 2 numbers
3. First solution was num1.append but it would add [1,2,[3,4]], then changed it to extend, which solved the issue
4. combining concatenation and sorting saved me around 4ms in solution, beating 100 percentile, nums = sorted(nums1+nums2) which is pretty cool 
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #nums1.extend(nums2)
        #nums1.sort()

        nums = sorted(nums1 + nums2)
        l1 = len(nums)
        if l1%2 == 0:
            return (nums[l1//2-1]+nums[l1//2])/2
        else:
            return nums[l1//2]
