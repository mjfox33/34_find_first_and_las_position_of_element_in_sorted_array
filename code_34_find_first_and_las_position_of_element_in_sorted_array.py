class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums or not target in nums:
            return [-1,-1]
        n = len(nums)
        first_index = nums.index(target)
        nums.reverse()
        last_index = n -1 - nums.index(target)
        return [first_index, last_index]