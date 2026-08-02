class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num = sorted(nums)
        result = []
        
        for i in range(len(num) - 2):
            left = i + 1
            right = len(num) - 1
            
            if i > 0 and num[i] == num[i - 1]:
                continue
                
            while left < right:
                total = num[i] + num[left] + num[right]
                
                if total == 0:
                    result.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result