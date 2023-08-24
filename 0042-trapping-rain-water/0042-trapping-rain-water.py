class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height)<=2:
            return 0

        left = 0
        right = len(height)-1

        left_height = height[left]
        right_height = height[right]

        water = 0

        while left < right:
            left_height = max(height[left], left_height)
            right_height = max(height[right], right_height)

            if left_height <= right_height:
                water += left_height-height[left]
                left+=1

            else:
                water += right_height - height[right]
                right-=1

        return water
