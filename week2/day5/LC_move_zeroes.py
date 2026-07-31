class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_zero = 0
        for n in range(len(nums)):
            if nums[n]!=0:
                nums[last_zero],nums[n] = nums[n],nums[last_zero]
                last_zero+=1
