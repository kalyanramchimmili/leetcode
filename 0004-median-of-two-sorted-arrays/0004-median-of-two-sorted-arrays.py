class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l1 = len(nums1)
        if l1%2 == 0:
            return (nums1[l1//2-1]+nums1[l1//2])/2
        else:
            return nums1[l1//2]