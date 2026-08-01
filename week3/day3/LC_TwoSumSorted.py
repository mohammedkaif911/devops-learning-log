class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_num = numbers[left] + numbers[right]
            
            if current_num == target:
                return [left + 1, right + 1] # 1-indexed output mapping
            elif current_num < target:
                left += 1
            else:
                right -= 1