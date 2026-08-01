# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:

#         for i in set(nums):
#             if nums.count(i)>len(nums)/2:
#                 return i
        
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        threshold = len(nums) // 2 # Double-slash executes integer division
        
        for n in nums:
            # Get current count of n, default to 0, and add 1
            counts[n] = counts.get(n, 0) + 1
            
            # Instant exit check
            if counts[n] > threshold:
                return n
