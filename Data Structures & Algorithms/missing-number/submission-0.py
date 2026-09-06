class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        given_sum = sum(nums)
        actual_sum = len(nums) * (len(nums) + 1) //2
        return actual_sum - given_sum