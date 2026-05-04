class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l == 2:
            return min(height[0], height[1])
        else:
            left = 0
            right = l - 1
            qnt = 0
            while (left < right):
                qnt = max(qnt, ((right-left) * min(height[left], height[right])))
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        return qnt