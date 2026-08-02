class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initialize the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            # Add the entering element, subtract the leaving element
            current_sum = current_sum + nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum / k