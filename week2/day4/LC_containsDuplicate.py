class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # If sizes do not match, a duplicate was purged
        return len(set(nums)) != len(nums)
