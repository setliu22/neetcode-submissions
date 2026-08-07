class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        ans = 0

        while left <= right:
            if leftMax <= rightMax:
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                right -= 1
        
        return ans

