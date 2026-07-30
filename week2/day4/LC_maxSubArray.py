class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]  # Initialize to first element as baseline
        current_sum = 0
        
        for n in nums:
            current_sum = current_sum + n
            
            # Independent Check 1: Update absolute record
            if current_sum > max_sum:
                max_sum = current_sum
                
            # Independent Check 2: Reset dead weight
            if current_sum < 0:
                current_sum = 0
                
        return max_sum
