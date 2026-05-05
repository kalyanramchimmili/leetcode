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
