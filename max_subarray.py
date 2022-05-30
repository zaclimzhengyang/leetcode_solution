class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not sum:
            return None
        if len(nums) == 1:
            return nums[0]

        maxSum = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
