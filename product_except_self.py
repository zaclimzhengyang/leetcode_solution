class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = result[i] * prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result

