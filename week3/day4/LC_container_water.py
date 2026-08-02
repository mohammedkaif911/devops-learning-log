class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_area = 0
        
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                area = (right_ptr - left_ptr) * height[left_ptr]
                left_ptr += 1
            else:
                area = (right_ptr - left_ptr) * height[right_ptr]
                right_ptr -= 1
                
            if area > max_area:
                max_area = area
                
        return max_area