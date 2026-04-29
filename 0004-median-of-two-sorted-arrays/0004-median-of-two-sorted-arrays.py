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