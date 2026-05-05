"""
1. similar to the prev 3-sum problem
2. one fixed var and a left and right pointer, sort the array to begin with and get the sum of min 3 elements as a baseline
3. for fixed from 0 to n-2, if the sum is equal to target best match return the target or curr_sum
4. if the diff btw the curr sum and target is lower than ans then replace ans with curr sum.
5. if the sum is grater than target dec right else inc left, return the final ans

time comp:- O(n^2)
space comp:- O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for fixed in range(n - 2):
            left = fixed + 1
            right = n - 1

            while left < right:
                curr_sum = nums[fixed] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum

                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans
